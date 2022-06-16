from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Save signals
@receiver(post_save, sender=OrderLineCase)
def update_on_case_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitems change
    """
    instance.order.update_total()

@receiver(post_save, sender=OrderLineCpu)
def update_on_cpu_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitems change
    """
    instance.order.update_total()

@receiver(post_save, sender=OrderLineGpu)
def update_on_gpu_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitems change
    """
    instance.order.update_total()

@receiver(post_save, sender=OrderLineMotherboard)
def update_on_mobo_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitems change
    """
    instance.order.update_total()

@receiver(post_save, sender=OrderLinePsu)
def update_on_psu_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitems change
    """
    instance.order.update_total()

@receiver(post_save, sender=OrderLineRam)
def update_on_ram_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitems change
    """
    instance.order.update_total()

@receiver(post_save, sender=OrderLineStorage)
def update_on_storage_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitems change
    """
    instance.order.update_total()


# Delete signals
@receiver(post_delete, sender=OrderLineCase)
def update_on_case_delete(sender, instance, **kwargs):
    """
    Update order total on lineitems delete
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineCpu)
def update_on_cpu_delete(sender, instance, **kwargs):
    """
    Update order total on lineitems delete
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineGpu)
def update_on_gpu_delete(sender, instance, **kwargs):
    """
    Update order total on lineitems delete
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineMotherboard)
def update_on_mobo_delete(sender, instance, **kwargs):
    """
    Update order total on lineitems delete
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLinePsu)
def update_on_psu_delete(sender, instance, **kwargs):
    """
    Update order total on lineitems delete
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineRam)
def update_on_ram_delete(sender, instance, **kwargs):
    """
    Update order total on lineitems delete
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineStorage)
def update_on_storage_delete(sender, instance, **kwargs):
    """
    Update order total on lineitems delete
    """
    instance.order.update_total()
