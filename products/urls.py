from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('', views.AllProductsView.as_view(), name='products'),
    path('add_product/', login_required(views.AdminProductView.as_view()), name='admin_add_product'),
    path('<str:category>/<int:id>/<str:operation>/', login_required(views.ManageProduct.as_view()), name='admin_edit_product'),
    path('<str:category>/<int:id>/', views.ProductDetails.as_view(), name='product_details'),
]
