from django.db import models

# Create your models here.


class Merchant(models.Model):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=200)
    address = models.TextField()
