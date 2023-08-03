from django.contrib import admin
from .models import Testimonials
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Testimonials)
class TestimonialsAdmin(SummernoteModelAdmin):
    """ To show summernote widget on the admin page """

    list_display = ('title', 'slug', 'status', 'created', 'updated', 'author')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
