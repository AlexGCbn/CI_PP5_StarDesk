from django.shortcuts import render, reverse, redirect
from django.views import View
from django.contrib import messages
from .forms import OrderForm


class CheckoutView(View):
    """
    Checkout class view
    """
    def get(self, request):
        """
        GET request view for checkout
        """
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, 'Nothing found in bag. Please add some items.')
            return redirect(reverse('products'))
        
        order_form = OrderForm()
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
        }

        return render(request, template, context)
