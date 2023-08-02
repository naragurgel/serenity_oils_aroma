from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))


class Testimonials(models.Model):
    """Testimonials model"""

    title = models.CharField(max_length=254)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testimonial")
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Testimonials, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Testimonials'
        """Sorts testimonials in descending order"""
        ordering = ["-created"]

    def __str__(self):
        return self.title
