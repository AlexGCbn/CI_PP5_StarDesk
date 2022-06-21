from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages

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

    def post(self, request, *args, **kwargs):
        """
        Post view to handle profile update
        """
        current_profile = get_object_or_404(UserProfile, user=request.user)
        form = ProfileForm(request.POST, instance=current_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile information updated successfully!')
        return redirect('profile_view')
