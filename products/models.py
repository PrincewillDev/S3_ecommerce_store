from django.db import models
from vendors.models import Store
import uuid
from datetime import datetime
# Create your models here.

class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100, null=False, blank=False)
    product_description = models.TextField(max_length=225, null=False, blank=False)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return self.product_name + " - " + self.product_description + " - " + str(self.product_price)
    
