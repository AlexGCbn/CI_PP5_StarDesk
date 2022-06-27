from decimal import Decimal
from django.conf import settings
from home.models import (
    DealCase, DealMotherboard,
    DealCpu, DealGpu, DealRam,
    DealPsu, DealStorage
)
from products.models import (
    Case, Motherboard,
    Cpu, Gpu, Ram,
    Psu, Storage
)


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item, quantity in bag.items():
        item_split = item.split('_')
        item_cat = item_split[0]
        item_id = item_split[1]

        if item_cat == 'case':
            product = Case.objects.get(id=item_id)
            deal_items = DealCase.objects.filter(product=product)
            if deal_items:
                for deal_item in deal_items:
                    if deal_item.get_days_remaining() > 0:
                        product.price = deal_item.price_new
        elif item_cat == 'motherboard':
            product = Motherboard.objects.get(id=item_id)
            deal_items = DealMotherboard.objects.filter(product=product)
            if deal_items:
                for deal_item in deal_items:
                    if deal_item.get_days_remaining() > 0:
                        product.price = deal_item.price_new
        elif item_cat == 'cpu':
            product = Cpu.objects.get(id=item_id)
            deal_items = DealCpu.objects.filter(product=product)
            if deal_items:
                for deal_item in deal_items:
                    if deal_item.get_days_remaining() > 0:
                        product.price = deal_item.price_new
        elif item_cat == 'gpu':
            product = Gpu.objects.get(id=item_id)
            deal_items = DealGpu.objects.filter(product=product)
            if deal_items:
                for deal_item in deal_items:
                    if deal_item.get_days_remaining() > 0:
                        product.price = deal_item.price_new
        elif item_cat == 'ram':
            product = Ram.objects.get(id=item_id)
            deal_items = DealRam.objects.filter(product=product)
            if deal_items:
                for deal_item in deal_items:
                    if deal_item.get_days_remaining() > 0:
                        product.price = deal_item.price_new
        elif item_cat == 'psu':
            product = Psu.objects.get(id=item_id)
            deal_items = DealPsu.objects.filter(product=product)
            if deal_items:
                for deal_item in deal_items:
                    if deal_item.get_days_remaining() > 0:
                        product.price = deal_item.price_new
        else:
            product = Storage.objects.get(id=item_id)
            deal_items = DealStorage.objects.filter(product=product)
            if deal_items:
                for deal_item in deal_items:
                    if deal_item.get_days_remaining() > 0:
                        product.price = deal_item.price_new

        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_cat': item_cat,
            'item_id': item_id,
            'quantity': quantity,
            'product': product
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
