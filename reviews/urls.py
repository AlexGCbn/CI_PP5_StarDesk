from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('add_review/<str:category>/<int:id>/', login_required(views.AddReview.as_view()), name='add_review'),
]
