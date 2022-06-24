from django.shortcuts import render
from django.views import generic, View


class IndexView(View):
    """ Basic index view """

    def get(self, request):
        """ A view to return index page """
        template = 'home/index.html'
        return render(request, template)

