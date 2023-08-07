from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def handler403(request, exception):
    """ Error Handler 403 - Forbidden Error Variations """
    return render(request, "errors/403.html", status=403)


def handler500(request):
    """ Error Handler 500 - Server Error """
    return render(request, "errors/500.html", status=500)


def handler400(request, exception):
    """ Error Handler 400 - Bad Request """
    return render(request, "errors/400.html", status=400)


def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['receiver@gmail.com',]
    send_mail(subject, message, email_from, recipient_list)
    return redirect('redirect to a new page')
