from django.db import models
from users.models import User
from datetime import datetime
import uuid

# Create your models here.
class Vendor(models.Model):
    vendor_id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

class Store(models.Model):
    store_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=100, null=False, blank=False)
    store_description = models.TextField(max_length=225, null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return self.store_name + " - " + self.store_description
    
class inventory(models.Model):
    inventory_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_id = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return str(self.quantity) + " - " + str(self.product_id) + " - " + str(self.created_at)