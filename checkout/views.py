from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.conf import settings
from django.views import View
from django.contrib import messages
import stripe
from products.models import Case, Motherboard, Cpu, Gpu, Ram, Psu, Storage
from bag.contexts import bag_contents
from .models import Order, OrderLineCase, OrderLineCpu, OrderLineGpu, OrderLineMotherboard, OrderLinePsu, OrderLineRam, OrderLineStorage
from .forms import OrderForm


class CheckoutView(View):
    """
    Checkout class view
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key

    order_form = OrderForm()
    template = 'checkout/checkout.html'

    def get(self, request, *args, **kwargs):
        """
        GET request view for checkout
        """
        bag = request.session.get('bag', {})
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

        context = {
            'order_form': self.order_form,
            'stripe_public_key': self.stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        """
        Checkout POST functionality
        """
        bag = request.session.get('bag', {})
        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)

        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if not bag:
            messages.error(request, 'Nothing found in bag. Please add some items.')
            return redirect(reverse('products'))
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'city': request.POST['city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item, quantity in bag.items():
                print(bag.items())
                try:
                    item_split = item.split('_')
                    item_cat = item_split[0]
                    item_id = item_split[1]

                    if item_cat == 'case':
                        product = Case.objects.get(id=item_id)
                        order_line_item = OrderLineCase(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                        order_line_item.save()
                    elif item_cat == 'motherboard':
                        product = Motherboard.objects.get(id=item_id)
                        order_line_item = OrderLineMotherboard(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                        order_line_item.save()
                    elif item_cat == 'cpu':
                        product = Cpu.objects.get(id=item_id)
                        order_line_item = OrderLineCpu(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                        order_line_item.save()
                    elif item_cat == 'gpu':
                        product = Gpu.objects.get(id=item_id)
                        order_line_item = OrderLineGpu(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                        order_line_item.save()
                    elif item_cat == 'ram':
                        product = Ram.objects.get(id=item_id)
                        order_line_item = OrderLineRam(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                        order_line_item.save()
                    elif item_cat == 'psu':
                        product = Psu.objects.get(id=item_id)
                        order_line_item = OrderLinePsu(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                        order_line_item.save()
                    else:
                        product = Storage.objects.get(id=item_id)
                        order_line_item = OrderLineStorage(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                        order_line_item.save()
                    
                except Exception as exception_error:
                    messages.error(request, f'Error: {exception_error}')
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            messages.success(request, f'Your order was successfully processed! \
                Order number: {order.order_number}')
            del request.session['bag']
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your order form. \
                Please check your form again.')


class CheckoutSuccessView(View):
    """
    Checkout success class view
    """
    template = 'checkout/checkout_success.html'
    
    def get(self, request, order_number, *args, **kwargs):
        """
        GET request view for checkout success
        """
        save_info = request.session.get('save_info')
        order = get_object_or_404(Order, order_number = order_number)
        context = {
            'order': order,
        }

        return render(request, self.template, context)
