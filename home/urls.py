from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('add_deal/<str:category>/<int:id>/', login_required(views.AdminAddDeal.as_view()), name='add_deal'),
]
