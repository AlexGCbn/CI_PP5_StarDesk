from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('add_deal/<str:category>/<int:id>/', views.AdminAddDeal.as_view(), name='add_deal'),
]
