import json
from django.shortcuts import (
    render, reverse,
    redirect, get_object_or_404,
    HttpResponse
)
from django.views.decorators.http import require_POST
from django.conf import settings
from django.views import View
from django.contrib import messages
import stripe
from products.models import Case, Motherboard, Cpu, Gpu, Ram, Psu, Storage
from bag.contexts import bag_contents
from profiles.forms import ProfileForm
from profiles.models import UserProfile
from .models import (
    Order, OrderLineCase,
    OrderLineCpu, OrderLineGpu,
    OrderLineMotherboard, OrderLinePsu,
    OrderLineRam, OrderLineStorage
)
from .forms import OrderForm


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'There was a problem processing \
            your payment. Please try again later.')
        return HttpResponse(content=e, status=400)


class CheckoutView(View):
    """
    Checkout class view
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key

    template = 'checkout/checkout.html'

    def get(self, request, *args, **kwargs):
        """
        GET request view for checkout
        """
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY
        stripe.api_key = stripe_secret_key
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(
                request, "There's nothing in your bag at the moment"
            )
            return redirect(reverse('products'))
        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)

        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        order_form = OrderForm()

        if request.user.is_authenticated:
            user_profile = UserProfile.objects.get(user=request.user)
            if user_profile:
                order_form = OrderForm(initial={
                    'full_name': user_profile.profile_full_name,
                    'email': request.user.email,
                    'phone_number': user_profile.profile_phone_number,
                    'country': user_profile.profile_country,
                    'postcode': user_profile.profile_postcode,
                    'city': user_profile.profile_city,
                    'street_address1': user_profile.profile_street_address1,
                    'street_address2': user_profile.profile_street_address2,
                })

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you set it up in your environment?')

        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        """
        Checkout POST functionality
        """
        stripe_secret_key = settings.STRIPE_SECRET_KEY
        stripe.api_key = stripe_secret_key
        bag = request.session.get('bag', {})

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
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            if request.user.is_authenticated:
                order.user = request.user
            order.original_bag = json.dumps(bag)
            order.save()
            for item, quantity in bag.items():
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

            # request.session['save_info'] = 'save-info' in request.POST
            if 'save-info' in request.POST and request.user.is_authenticated:
                profile = UserProfile.objects.get(user=request.user)
                save_data = {
                    'profile_full_name': order.full_name,
                    'profile_phone_number': order.phone_number,
                    'profile_postcode': order.postcode,
                    'profile_city': order.city,
                    'profile_street_address1': order.street_address1,
                    'profile_street_address2': order.street_address2,
                    'profile_country': order.country,
                }
                profile_form = ProfileForm(save_data, instance=profile)
                if profile_form.is_valid():
                    profile_form.save()
            messages.success(request, f'Your order was successfully processed! \
                Order number: {order.order_number}')
            return redirect(reverse(
                'checkout_success', args=[order.order_number]
            ))
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
        order = get_object_or_404(Order, order_number=order_number)
        product_list = []
        if 'bag' in request.session:
            del request.session['bag']

        for item in (
            order.lineitem_case,
            order.lineitem_motherboard,
            order.lineitem_cpu,
            order.lineitem_gpu,
            order.lineitem_ram,
            order.lineitem_psu,
            order.lineitem_storage
        ):
            try:
                item_object = item.all()
                for product in item_object:
                    product_list.append(product)
            except Exception:
                continue
        context = {
            'order': order,
            'product_list': product_list,
        }

        return render(request, self.template, context)
