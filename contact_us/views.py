from django.shortcuts import render
from .models import ContactUs


def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactUs.objects.create(
            name=name, email=email, subject=subject, message=message)

    return render(request, 'contact_us/contact_us.html')

