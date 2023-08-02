from django.shortcuts import render, redirect
from .forms import ContactUsForm


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_us/success_page.html')
    else:
        form = ContactUsForm()

    return render(request, 'contact_us/contact_us.html', {'form': form})


def success_page(request):
    return render(request, 'contact_us/success_page.html')
