from django.db import models
from django.db.models import signals
from django.dispatch import receiver


class Merchant(models.Model):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=200)
    address = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)


@receiver(signals.post_save, sender=Product)
def create_product(sender, instance, **kwargs):
    print("Save method is called")


@receiver(signals.pre_save, sender=Product)
def check_product_description(sender, instance, **kwargs):
    if not instance.description:
        instance.description = "This is Default Description"
