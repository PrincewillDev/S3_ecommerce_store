from django.db import models
from users.models import User
from products.models import Product
from datetime import datetime
import uuid

# Create your models here.
class cart(models.Model):
    cart_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
    added_at = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return str(self.cart_id) + " - " + str(self.user_id) + " - " + str(self.product_id) + " - " + str(self.quantity) + " - " + str(self.added_at)