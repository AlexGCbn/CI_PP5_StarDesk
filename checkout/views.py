from django.shortcuts import render, reverse, redirect
from django.conf import settings
from django.views import View
from django.contrib import messages
from .forms import OrderForm
from bag.contexts import bag_contents
import stripe


class CheckoutView(View):
    """
    Checkout class view
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key

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

        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if not self.stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you set it up in your environment?')

        order_form = OrderForm()
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': self.stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)
