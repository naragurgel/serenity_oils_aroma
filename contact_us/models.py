from django.db import models


class ContactUs(models.Model):
    """
    Define the model fields
    fields: 'name', 'email', 'subject' and 'message'
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.subject
