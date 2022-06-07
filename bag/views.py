from django.shortcuts import render, redirect
from django.views import View


class BagView(View):
    """ Bag class view """

    def get(self, request):
        """ GET request view for Bag """

        template = 'bag/bag.html'
        return render(request, template)

    def post(self, request, category, item_id):
        """ POST request for adding items to Bag """

        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')
        bag = request.session.get('bag', {})

        item = category + item_id
        if item in list(bag.keys()):
            bag[item] += quantity
        else:
            bag[item] = quantity

        request.session['bag'] = bag
        return redirect(redirect_url)
