from django.db import models
from users.models import User
from products.models import Product
from datetime import datetime
import uuid

# Create your models here.
class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return str(self.order_id) + " - " + str(self.user_id) + " - " + str(self.created_at)
    

class OrderDetails(models.Model):
        order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
        product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
        quantity = models.IntegerField(null=False, blank=False)

        def __str__(self):
            return str(self.order.order_id) + " - " + str(self.product.product_name) + " - " + str(self.quantity)

class Order_status(models.Model):
    order_status_id = models.IntegerField(primary_key=True, default=uuid.uuid4, editable=False)
    order_status= models.CharField(blank=False, null=False, max_length=70)
    

class Userorderstatus(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_status_id = models.ForeignKey(Order_status, on_delete=models.CASCADE)

    def __str_(self):
        return str(self.user_id) + " - " + str(self.order_id) + " - " + str(self.order_status_id)
