from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    User profile model to save profile information
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )
    profile_full_name = models.CharField(
        max_length=50, null=True, blank=True
    )
    profile_phone_number = models.CharField(
        max_length=20, null=True, blank=True
    )
    profile_country = CountryField(
        blank_label='Country', null=True, blank=True
    )
    profile_postcode = models.CharField(
        max_length=20, null=True, blank=True
    )
    profile_city = models.CharField(
        max_length=40, null=True, blank=True
    )
    profile_street_address1 = models.CharField(
        max_length=80, null=True, blank=True
    )
    profile_street_address2 = models.CharField(
        max_length=80, null=True, blank=True
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def user_profile_create(sender, instance, created, **kwargs):
    """
    Create or update user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
