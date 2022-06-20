from django.shortcuts import render
from django.views import View


class ProfileView(View):
    """
    Class based view for User Profiles
    """
    template = 'profiles/profile.html'

    def get(self, request, *args, **kwargs):
        """
        GET request view for User Profiles
        """
        context = {}
        return render(request, self.template, context)
