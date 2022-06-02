from django.shortcuts import render
from django.views import View


class ViewBag(View):
    """ Bag class view """

    def get(self, request):
        """ GET request view for Bag """

        template = 'bag/bag.html'
        return render(request, template)
