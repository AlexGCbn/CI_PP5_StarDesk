from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import UserProfile
from checkout.models import Order
from .forms import ProfileForm


class ProfileView(View):
    """
    Class based view for User Profiles
    """
    template = 'profiles/profile.html'

    def get(self, request, *args, **kwargs):
        """
        GET request view for User Profiles
        """
        current_profile = get_object_or_404(UserProfile, user=request.user)
        order_history = Order.objects.filter(user=request.user)

        form = ProfileForm(instance=current_profile)
        context = {
            'form': form,
            'orders': order_history,
        }
        return render(request, self.template, context)