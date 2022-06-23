from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.models import User
from products.models import Case, Motherboard, Cpu, Gpu, Ram, Psu, Storage
from profiles.models import UserProfile
from .models import Order, OrderLineCase, OrderLineCpu, OrderLineGpu, OrderLineMotherboard, OrderLinePsu, OrderLineRam, OrderLineStorage

import json
import time


class StripeWH_Handler:
    """
    Handle Stripe webhooks
    """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Handle sending the confirmation email
        """
        customer_email = order.email
        products = []
        for item in (
            order.lineitem_case,
            order.lineitem_mobo,
            order.lineitem_cpu,
            order.lineitem_gpu,
            order.lineitem_ram,
            order.lineitem_psu,
            order.lineitem_storage):
            try:
                item_object = item.get()
                products.append(item_object)
            except Exception:
                continue
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {
                'order': order,
                'contact_email': settings.DEFAULT_FROM_EMAIL,
                'products': products,
            }
        )
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            customer_email,
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
     
        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.profile_phone_number = shipping_details.phone
                profile.profile_country = shipping_details.address.country
                profile.profile_postcode = shipping_details.address.postal_code
                profile.profile_city = shipping_details.address.city
                profile.profile_street_address1 = shipping_details.address.line1
                profile.profile_street_address2 = shipping_details.address.line2
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order_user = User.objects.get(username=intent.metadata.username)
                order = Order.objects.create(
                    user=order_user,
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item, quantity in json.loads(bag).items():
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
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
