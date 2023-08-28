from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Testimonials
from checkout.models import Order
from django.contrib.auth.models import User
from .forms import TestimonialForm


def testimonial_list(request):
    """ Function to display testimonials
       and to check if the user made any orders """

    queryset = Testimonials.objects.filter(status=1).order_by("-created")

    if request.user.is_authenticated:
        queryset_author = queryset.filter(author=request.user)
        has_orders = Order.objects.filter(
            email=request.user.email).count() > 0

    else:
        queryset_author = None
        has_orders = False

    is_admin = request.user.is_superuser

    return render(
        request,
        'testimonials/testimonials.html',
        {
            'testimonials': queryset,
            'has_orders': has_orders,
            'queryset_author': queryset_author,
            'is_admin': is_admin,
        }
    )


def testimonial_detail(request, slug):
    """ Function to display testimonials details page
       and to check if the user made any orders """

    queryset = Testimonials.objects.filter(status=1)
    testimonial = get_object_or_404(queryset, slug=slug)

    if request.user.is_authenticated:
        queryset_author = queryset.filter(author=request.user)
        has_orders = Order.objects.filter(
            email=request.user.email).count() > 0

    else:
        queryset_author = None
        has_orders = False

    is_admin = request.user.is_superuser

    return render(
        request,
        "testimonials/testimonial_detail.html",
        {
            "testimonial": testimonial,
            'has_orders': has_orders,
            'queryset_author': queryset_author,
            'is_admin': is_admin,
        }
    )


@login_required
def add_testimonial(request):
    """ Add a testimonial to the store website """

    has_orders = Order.objects.filter(
        email=request.user.email).count() > 0
    if not has_orders:
        messages.error(
            request, 'Failed to add testimonial.'
            'Please oder something before adding a testimonial.')
        return redirect(reverse('testimonials'))

    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.author = request.user
            testimonial.status = 1
            testimonial.save()
            messages.success(request, 'Successfully added testimonial!')
            return redirect(reverse(
                'testimonials'))
        else:
            messages.error(
                request, 'Failed to add testimonial.'
                'Please ensure the form is valid.')
    else:
        form = TestimonialForm()

    template = 'testimonials/add_testimonial.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_testimonial(request, slug):
    """ Edit a testimonial """

    testimonial = get_object_or_404(Testimonials, slug=slug)
    if not testimonial.author and not request.user.is_admin == request.user:
        messages.error(request,
                       'Sorry, only author can edit a testimonial.'
                       )
        return redirect(reverse('testimonials'))

    has_orders = Order.objects.filter(
        email=request.user.email).count() > 0
    if not has_orders:
        messages.error(
            request, 'Failed to edit testimonial.'
            'Please oder something before adding a testimonial.')
        return redirect(reverse('testimonials'))

    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            testimonial = form.save()
            messages.success(request, 'Successfully edited testimonial!')
            return redirect(reverse(
                'testimonials'))
        else:
            messages.error(
                request, 'Failed to edit testimonial.'
                'Please ensure the form is valid.')
    else:
        form = TestimonialForm(instance=testimonial)

    template = 'testimonials/edit_testimonial.html'
    context = {
        'form': form,
        "testimonial": testimonial,
    }

    return render(request, template, context)


@login_required
def delete_testimonial(request, slug):
    """ Delete a testimonial from the store website """

    testimonial = get_object_or_404(Testimonials, slug=slug)

    if not (testimonial.author == request.user or request.user.is_superuser):
        messages.error(request,
                       'Sorry, only author or admin can delete testimonials.'
                       )
        return redirect(reverse('testimonials'))

    testimonial.delete()
    messages.success(request, 'Testimonial deleted!')
    return redirect(reverse('testimonials'))
