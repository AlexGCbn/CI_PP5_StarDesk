import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.contrib.auth.models import User

from django_countries.fields import CountryField
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


class Order(models.Model):
    order_number = models.CharField(
        max_length=32, null=False, editable=False
    )
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='order_user'
    )
    full_name = models.CharField(
        max_length=50, null=False, blank=False
    )
    email = models.EmailField(
        max_length=254, null=False, blank=False
    )
    phone_number = models.CharField(
        max_length=20, null=False, blank=False
    )
    country = CountryField(
        blank_label='Country *', null=False, blank=False
    )
    postcode = models.CharField(
        max_length=20, null=False, blank=False
    )
    city = models.CharField(
        max_length=40, null=False, blank=False
    )
    street_address1 = models.CharField(
        max_length=80, null=False, blank=False
    )
    street_address2 = models.CharField(
        max_length=80, null=True, blank=True
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    original_bag = models.TextField(
        null=False, blank=False, default=''
    )
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=''
    )

    def _generate_order_number(self):
        """
        Generate a random order number
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = (
            (self.lineitem_case.aggregate(
                Sum('lineitem_total'))['lineitem_total__sum'] or 0) +
            (self.lineitem_motherboard.aggregate(
                Sum('lineitem_total'))['lineitem_total__sum'] or 0) +
            (self.lineitem_cpu.aggregate(
                Sum('lineitem_total'))['lineitem_total__sum'] or 0) +
            (self.lineitem_gpu.aggregate(
                Sum('lineitem_total'))['lineitem_total__sum'] or 0) +
            (self.lineitem_ram.aggregate(
                Sum('lineitem_total'))['lineitem_total__sum'] or 0) +
            (self.lineitem_psu.aggregate(
                Sum('lineitem_total'))['lineitem_total__sum'] or 0) +
            (self.lineitem_storage.aggregate(
                Sum('lineitem_total'))['lineitem_total__sum'] or 0)
        )
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = (
                self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
            )
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Set order number on save
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """Main OrderLineItem model class"""
    quantity = models.IntegerField(
        null=False, blank=False, default=0
    )
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )

    def __str__(self):
        return f'Order item {self.product.manufacturer} {self.product.model}'

    class Meta:
        abstract = True


class OrderLineCase(OrderLineItem):
    """OrderLineCase submodel"""
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitem_case'
    )
    product = models.ForeignKey(
        Case, null=False, blank=False, on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        """
        Update lineitem_total on save
        """
        deal_items = DealCase.objects.filter(product=self.product)
        if deal_items:
            deal_price = self.product.price
            for deal_item in deal_items:
                if deal_item.get_days_remaining() > 0:
                    deal_price = deal_item.price_new
                else:
                    continue
            self.lineitem_total = deal_price * self.quantity
        else:
            self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)


class OrderLineMotherboard(OrderLineItem):
    """OrderLineMotherboard submodel"""
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitem_motherboard'
    )
    product = models.ForeignKey(
        Motherboard, null=False, blank=False, on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        """
        Update lineitem_total on save
        """
        deal_items = DealMotherboard.objects.filter(product=self.product)
        if deal_items:
            deal_price = self.product.price
            for deal_item in deal_items:
                if deal_item.get_days_remaining() > 0:
                    deal_price = deal_item.price_new
                else:
                    continue
            self.lineitem_total = deal_price * self.quantity
        else:
            self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)


class OrderLineCpu(OrderLineItem):
    """OrderLineCpu submodel"""
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitem_cpu'
    )
    product = models.ForeignKey(
        Cpu, null=False, blank=False, on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        """
        Update lineitem_total on save
        """
        deal_items = DealCpu.objects.filter(product=self.product)
        if deal_items:
            deal_price = self.product.price
            for deal_item in deal_items:
                if deal_item.get_days_remaining() > 0:
                    deal_price = deal_item.price_new
                else:
                    continue
            self.lineitem_total = deal_price * self.quantity
        else:
            self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)


class OrderLineGpu(OrderLineItem):
    """OrderLineGpu submodel"""
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitem_gpu'
    )
    product = models.ForeignKey(
        Gpu, null=False, blank=False, on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        """
        Update lineitem_total on save
        """
        deal_items = DealGpu.objects.filter(product=self.product)
        if deal_items:
            deal_price = self.product.price
            for deal_item in deal_items:
                if deal_item.get_days_remaining() > 0:
                    deal_price = deal_item.price_new
                else:
                    continue
            self.lineitem_total = deal_price * self.quantity
        else:
            self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)


class OrderLineRam(OrderLineItem):
    """OrderLineRam submodel"""
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitem_ram'
    )
    product = models.ForeignKey(
        Ram, null=False, blank=False, on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        """
        Update lineitem_total on save
        """
        deal_items = DealRam.objects.filter(product=self.product)
        if deal_items:
            deal_price = self.product.price
            for deal_item in deal_items:
                if deal_item.get_days_remaining() > 0:
                    deal_price = deal_item.price_new
                else:
                    continue
            self.lineitem_total = deal_price * self.quantity
        else:
            self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)


class OrderLinePsu(OrderLineItem):
    """OrderLinePsu submodel"""
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitem_psu'
    )
    product = models.ForeignKey(
        Psu, null=False, blank=False, on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        """
        Update lineitem_total on save
        """
        deal_items = DealPsu.objects.filter(product=self.product)
        if deal_items:
            deal_price = self.product.price
            for deal_item in deal_items:
                if deal_item.get_days_remaining() > 0:
                    deal_price = deal_item.price_new
                else:
                    continue
            self.lineitem_total = deal_price * self.quantity
        else:
            self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)


class OrderLineStorage(OrderLineItem):
    """OrderLineStorage submodel"""
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitem_storage'
    )
    product = models.ForeignKey(
        Storage, null=False, blank=False, on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        """
        Update lineitem_total on save
        """
        deal_items = DealStorage.objects.filter(product=self.product)
        if deal_items:
            deal_price = self.product.price
            for deal_item in deal_items:
                if deal_item.get_days_remaining() > 0:
                    deal_price = deal_item.price_new
                else:
                    continue
            self.lineitem_total = deal_price * self.quantity
        else:
            self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)
