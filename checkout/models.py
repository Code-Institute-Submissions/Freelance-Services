from django.db import models
from services.models import Service
# Create your models here.

class Order(models.Model):
    """
    Used to define what an order form should contain, returns id, date and name for Freelancer to view details. 
    """
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=40, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    """
    Used to describe an Order Line Item, 
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.service.name, self.service.price)
