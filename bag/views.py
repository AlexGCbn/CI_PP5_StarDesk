from django.shortcuts import render, redirect
from django.views import View


class BagView(View):
    """ Bag class view """

    def get(self, request):
        """ GET request view for Bag """

        template = 'bag/bag.html'
        return render(request, template)

    # Temporary
    def post(self, request):
        """ POST request for updating/removing Bag items """

        
        redirect_url = request.POST.get('redirect_url')
        bag = request.session.get('bag', {})
        item = request.POST.get('product_pass')

        if request.POST.get('operation') == 'update':
            quantity = int(request.POST.get('value'))
            bag[item] = quantity


        request.session['bag'] = bag
        return redirect(redirect_url)
