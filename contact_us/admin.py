from django.contrib import admin
from .models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'subject',
        'message',
    )

    ordering = ('subject',)


admin.site.register(ContactUs, ContactUsAdmin)
