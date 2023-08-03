from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Testimonials


class TestimonialForm(forms.ModelForm):
    """ Form to add a testimonial """

    title = forms.CharField(max_length=254)
    content = forms.CharField(widget=SummernoteWidget(), max_length=1000)

    class Meta:
        model = Testimonials
        fields = ('title', 'content')
