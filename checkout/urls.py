from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.CheckoutView.as_view(), name='checkout'),
    path('checkout_success/<order_number>', views.CheckoutSuccessView.as_view(), name='checkout_success'),
    path('wh', webhook, name='webhook'),
]
