from django.shortcuts import render, reverse, redirect
from django.conf import settings
from django.views import View
from django.contrib import messages
from .forms import OrderForm
from bag.contexts import bag_contents


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
        
        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        order_form = OrderForm()
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        }

        return render(request, template, context)
