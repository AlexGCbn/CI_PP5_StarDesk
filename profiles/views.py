from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import UserProfile


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
        context = {
            'profile': current_profile,
        }
        return render(request, self.template, context)
