from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.views import View


class BagView(View):
    """ Bag class view """

    def get(self, request):
        """ GET request view for Bag """

        template = 'bag/bag.html'
        return render(request, template)

    def post(self, request):
        """ POST request for updating/removing Bag items """
        try:
            bag = request.session.get('bag', {})
            item = request.POST.get('product_pass')
            product_name = request.POST.get('product_friendly_name')

            if request.POST.get('operation') == 'update':
                quantity = int(request.POST.get('value'))
                if quantity >= 1 and quantity <= 99:
                    bag[item] = quantity
                    messages.success(
                        request,
                        f'{product_name} quantity updated successfully.'
                    )
                else:
                    messages.warning(
                        request, 'Quantity needs to be between 1 and 99!'
                    )
                    return redirect(reverse('view_bag'))
            elif request.POST.get('operation') == 'remove':
                del bag[item]
                messages.success(request, f'{product_name} removed from bag.')

            request.session['bag'] = bag
            return redirect(reverse('view_bag'))
        except Exception as e:
            messages.error(request, f'Error: {e}')
            return redirect(reverse('view_bag'))
