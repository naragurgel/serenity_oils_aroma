from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse, HttpResponseRedirect
)
from django.http import Http404
from django.core import signing
from django.core.mail import send_mail
from django.utils.http import urlencode
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm, EmailForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.contexts import bag_contents
from django.core.mail import send_mail
from django.template.loader import render_to_string
import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    Handle the cache_checkout_data functionality
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Handle the chackout process
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "  # noqa
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            if request.user.is_authenticated:
                profile = UserProfile.objects.get(user=request.user)
                # Attach the user's profile to the order
                order.user_profile = profile
                order.save()

                # Save the user's info
                if 'save-info' in request.POST:
                    user_profile_form = UserProfileForm({f'default_{k}': v for k,v in order.items()}, instance=profile)
                    if user_profile_form.is_valid():
                        user_profile_form.save()
            if request.user.is_authenticated:
                return redirect(reverse('checkout_success', args=[order.order_number]))
            return redirect(generate_tokenized_link(order, request))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")  # noqa
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')  # noqa

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    View to handle the chackout_success process
    """
    order = get_object_or_404(Order, order_number=order_number)

    if not order.user_profile:

        # if token exists we check to see if the email is the same from order
        try: 
            # Max age of 15 minutes
            token = request.GET.get("token", '')
            data = signing.loads(token, max_age=900)
            email = data.get("email")
            if not email:
                return redirect("checkout/error_email.html")
            if email != order.email:
                return HttpResponseRedirect(reverse('errors/403.html'))
        except (signing.BadSignature, signing.SignatureExpired) as error:
            form = EmailForm()
            return render(request, 'checkout/email_form.html', {'form': form, 'order_number': order_number})
    elif order.user_profile.user != request.user:
        return HttpResponseRedirect(reverse('errors/403.html'))
    
    if not order.email_sent:
        email_to = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
            )
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
            )
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [email_to])  # noqa

        messages.success(request, f'Order successfully processed! \
            Your order number is {order_number}. A confirmation \
            email will be sent to {order.email}.')
        order.email_sent = True
        order.save()


    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


@require_POST
def checkout_confirm_email(request, order_number):
    """View to handle the confirmation email order"""
    order = get_object_or_404(Order, order_number=order_number)
    form = EmailForm(request.POST, instance=order)

    if not form.is_valid():
        return render(request, 'checkout/email_form.html', {'form': form, 'order_number': order_number})


    subject = render_to_string(
        'checkout/magic_link/magic_link_email_subject.txt',
        {'order': order})
    body = render_to_string(
        'checkout/magic_link/magic_link_email_body.txt',
        {
            'link': generate_tokenized_link(order, request),
            'order': order,
            'contact_email': settings.DEFAULT_FROM_EMAIL
        })
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [order.email]
    )
    return render(request, 'checkout/success_email.html')


def generate_tokenized_link(order, request):
    """View to generate the token for the magic link verification"""
    token = signing.dumps({'email': order.email})
    checkout_success_link = reverse('checkout_success',
                                    kwargs={
                                        'order_number': order.order_number}
                                    )
    access_link = f'{checkout_success_link}?{urlencode({"token": token})}'
    return request.build_absolute_uri(access_link)
