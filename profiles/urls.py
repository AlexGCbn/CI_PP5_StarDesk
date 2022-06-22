from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('', login_required(views.ProfileView.as_view()), name='profile_view'),
    path('order_history/<order_number>', login_required(views.OrderHistoryView.as_view()), name='order_history'),
]
