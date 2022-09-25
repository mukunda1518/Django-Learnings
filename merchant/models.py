from django.db import models

# Create your models here.


class Merchant(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
