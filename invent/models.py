from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ClientInventory(models.Model):
    item_No = models.IntegerField()
    client_id = models.ForeignKey(User,on_delete=models.CASCADE)
    item_SKU = models.CharField(max_length=50)
    item_description = models.CharField(max_length=50)
    item_price = models.DecimalField(max_digits=5,decimal_places=2)
    item_availability = models.IntegerField()
