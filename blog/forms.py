from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    # Define a form for creating and updating comments
    class Meta:
        model = Comment
        fields = ('body',)
