from django.db import models
from django.contrib.auth.models import User
from products.models import Case, Motherboard, Cpu, Gpu, Ram, Psu, Storage

RATING = (
    (1, 'Very Dissatisfied'),
    (2, 'Dissatisfied'),
    (3, 'Neutral'),
    (4, 'Satisfied'),
    (5, 'Very Satisfied')
)


class CaseReview(models.Model):
    """Review model for Case product"""
    product = models.ForeignKey(Case, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=RATING, default=3)
    comment = models.TextField(max_length=500, null=True, blank=True)


class MotherboardReview(models.Model):
    """Review model for Motherboard product"""
    product = models.ForeignKey(Motherboard, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=RATING, default=3)
    comment = models.TextField(max_length=500, null=True, blank=True)


class CpuReview(models.Model):
    """Review model for Cpu product"""
    product = models.ForeignKey(Cpu, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=RATING, default=3)
    comment = models.TextField(max_length=500, null=True, blank=True)


class GpuReview(models.Model):
    """Review model for Gpu product"""
    product = models.ForeignKey(Gpu, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=RATING, default=3)
    comment = models.TextField(max_length=500, null=True, blank=True)


class RamReview(models.Model):
    """Review model for Ram product"""
    product = models.ForeignKey(Ram, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=RATING, default=3)
    comment = models.TextField(max_length=500, null=True, blank=True)


class PsuReview(models.Model):
    """Review model for Psu product"""
    product = models.ForeignKey(Psu, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=RATING, default=3)
    comment = models.TextField(max_length=500, null=True, blank=True)


class StorageReview(models.Model):
    """Review model for Storage product"""
    product = models.ForeignKey(Storage, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=RATING, default=3)
    comment = models.TextField(max_length=500, null=True, blank=True)
