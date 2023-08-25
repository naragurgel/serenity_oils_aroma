from . import views
from django.urls import path

urlpatterns = [
    path("", views.testimonial_list, name="testimonials"),
    path('add/', views.add_testimonial, name='add_testimonial'),
    path('edit/<slug:slug>/', views.edit_testimonial, name='edit_testimonial'),
    path('delete/<slug:slug>/', views.delete_testimonial, name='delete_testimonial'),  # noqa
    path('<slug:slug>/', views.testimonial_detail, name='testimonial_detail'),
]
