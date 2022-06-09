from django.shortcuts import render, redirect, reverse
from django.views import View


class BagView(View):
    """ Bag class view """

    def get(self, request):
        """ GET request view for Bag """

        template = 'bag/bag.html'
        return render(request, template)

    def post(self, request):
        """ POST request for updating/removing Bag items """
        
        bag = request.session.get('bag', {})
        item = request.POST.get('product_pass')

        if request.POST.get('operation') == 'update':
            quantity = int(request.POST.get('value'))
            if quantity >= 1 and quantity <= 99:
                bag[item] = quantity
            else:
                # Add error message here
                return redirect(reverse('view_bag'))
        elif request.POST.get('operation') == 'remove':
            del bag[item]

        request.session['bag'] = bag
        return redirect(reverse('view_bag'))
