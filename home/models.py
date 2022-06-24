from django.db import models
from products.models import Case, Motherboard, Cpu, Gpu, Ram, Psu, Storage

import datetime


class DealProduct(models.Model):
    """Main product deal class"""
    price_new = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    deal_ends = models.DateField(null=False)

    def __str__(self):
        return f'{self.product.model} reduced to {self.price_new}'

    def get_days_remaining(self):
        """Return deal days remaining"""
        days_remaining = self.deal_ends - datetime.date.today()
        return days_remaining.days

    class Meta:
        abstract = True


class DealCase(DealProduct):
    """DealCase submodel to make Case deals/offers"""
    product = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='case_deal')


class DealMotherboard(DealProduct):
    """DealMotherboard submodel to make Case deals/offers"""
    product = models.ForeignKey(Motherboard, on_delete=models.CASCADE, related_name='motherboard_deal')


class DealCpu(DealProduct):
    """DealCpu submodel to make Case deals/offers"""
    product = models.ForeignKey(Cpu, on_delete=models.CASCADE, related_name='cpu_deal')


class DealGpu(DealProduct):
    """DealGpu submodel to make Case deals/offers"""
    product = models.ForeignKey(Gpu, on_delete=models.CASCADE, related_name='gpu_deal')


class DealRam(DealProduct):
    """DealRam submodel to make Case deals/offers"""
    product = models.ForeignKey(Ram, on_delete=models.CASCADE, related_name='ram_deal')


class DealPsu(DealProduct):
    """DealPsu submodel to make Case deals/offers"""
    product = models.ForeignKey(Psu, on_delete=models.CASCADE, related_name='psu_deal')


class DealStorage(DealProduct):
    """DealStorage submodel to make Case deals/offers"""
    product = models.ForeignKey(Storage, on_delete=models.CASCADE, related_name='storage_deal')
