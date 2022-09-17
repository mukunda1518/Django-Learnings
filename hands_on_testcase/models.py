from django.db import models

# Create your models here.


class RideRequest(models.Model):
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    travel_date_time = models.DateTimeField(null=True, blank=True)
    luggage_quantity = models.IntegerField()
