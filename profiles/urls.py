from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile_view'),
    path('order_history/<order_number>', views.OrderHistoryView.as_view(), name='order_history'),
]
