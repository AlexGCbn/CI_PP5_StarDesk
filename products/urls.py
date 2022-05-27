from django.urls import path
from . import views


urlpatterns = [
    path('', views.AllProductsView.as_view(), name='products'),
    path('<str:category>/<int:id>/', views.ProductDetails.as_view(), name='product_details'),
]
