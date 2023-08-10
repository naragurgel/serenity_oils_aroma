from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    """
    ContactUsForm model form for user contact submissions
    """
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        """
        Initialize form with crispy forms helper and submit button
        """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(
            Submit('submit', 'Submit', css_class='btn-primary'))
