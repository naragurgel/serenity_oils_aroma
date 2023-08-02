from django.urls import path
from . import views

urlpatterns = [
    path('', views.testimonial_list, name='testimonial_list'),
    path('<slug:slug>/', views.testimonial_detail, name='testimonial_detail'),
    path('add/', views.add_testimonial, name='add_testimonial'),
    path('<slug:slug>/edit/', views.edit_testimonial, name='edit_testimonial'),
]
