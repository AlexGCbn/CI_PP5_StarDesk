from django.db import models
from products.models import Case, Motherboard, Cpu, Gpu, Ram, Psu, Storage


class DealCase(models.Model):
    """DealCase model to make Case deals/offers"""
    product = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='case_deal')
    price_was = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    price_new = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    deal_ends = models.DateTimeField(null=False)

    def __str__(self):
        return f'{self.product.model} reduced to {self.price_new}'

    def update_price_was(self):
        """Update price_was on object creation"""
        self.price_was = self.product.price
        self.save()


class DealMotherboard(models.Model):
    """DealCase model to make Case deals/offers"""
    product = models.ForeignKey(Motherboard, on_delete=models.CASCADE, related_name='motherboard_deal')
    price_was = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    price_new = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    deal_ends = models.DateTimeField(null=False)

    def __str__(self):
        return f'{self.product.model} reduced to {self.price_new}'

    def update_price_was(self):
        """Update price_was on object creation"""
        self.price_was = self.product.price
        self.save()


class DealCpu(models.Model):
    """DealCase model to make Case deals/offers"""
    product = models.ForeignKey(Cpu, on_delete=models.CASCADE, related_name='cpu_deal')
    price_was = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    price_new = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    deal_ends = models.DateTimeField(null=False)

    def __str__(self):
        return f'{self.product.model} reduced to {self.price_new}'

    def update_price_was(self):
        """Update price_was on object creation"""
        self.price_was = self.product.price
        self.save()


class DealGpu(models.Model):
    """DealCase model to make Case deals/offers"""
    product = models.ForeignKey(Gpu, on_delete=models.CASCADE, related_name='gpu_deal')
    price_was = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    price_new = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    deal_ends = models.DateTimeField(null=False)

    def __str__(self):
        return f'{self.product.model} reduced to {self.price_new}'

    def update_price_was(self):
        """Update price_was on object creation"""
        self.price_was = self.product.price
        self.save()


class DealRam(models.Model):
    """DealCase model to make Case deals/offers"""
    product = models.ForeignKey(Ram, on_delete=models.CASCADE, related_name='ram_deal')
    price_was = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    price_new = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    deal_ends = models.DateTimeField(null=False)

    def __str__(self):
        return f'{self.product.model} reduced to {self.price_new}'

    def update_price_was(self):
        """Update price_was on object creation"""
        self.price_was = self.product.price
        self.save()


class DealPsu(models.Model):
    """DealCase model to make Case deals/offers"""
    product = models.ForeignKey(Psu, on_delete=models.CASCADE, related_name='psu_deal')
    price_was = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    price_new = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    deal_ends = models.DateTimeField(null=False)

    def __str__(self):
        return f'{self.product.model} reduced to {self.price_new}'

    def update_price_was(self):
        """Update price_was on object creation"""
        self.price_was = self.product.price
        self.save()


class DealStorage(models.Model):
    """DealCase model to make Case deals/offers"""
    product = models.ForeignKey(Storage, on_delete=models.CASCADE, related_name='storage_deal')
    price_was = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    price_new = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    deal_ends = models.DateTimeField(null=False)

    def __str__(self):
        return f'{self.product.model} reduced to {self.price_new}'

    def update_price_was(self):
        """Update price_was on object creation"""
        self.price_was = self.product.price
        self.save()
