from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),  # noqa
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),  # noqa
    path('checkout_confirm_email/<order_number>', views.checkout_confirm_email, name='checkout_confirm_email'),  # noqa
    path('wh/', webhook, name='webhook'),
]
