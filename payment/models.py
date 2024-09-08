from django.db import models
from orders.models import Order
from datetime import datetime
import uuid
from users.models import User

# Create your models here.
class Payment(models.Model):
    payment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

class PaymentStatus(models.Model):
    payment_status_id = models.IntegerField(primary_key=True, default=uuid.uuid4, editable=False)
    payment_status= models.CharField(blank=False, null=False, max_length=70)

class PaymentMethod(models.Model):
    payment_method_id = models.IntegerField(primary_key=True, default=uuid.uuid4, editable=False)
    payment_method= models.CharField(blank=False, null=False, max_length=70)

class Paymentuser(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    payment_status_id = models.ForeignKey(PaymentStatus, on_delete=models.CASCADE)

    def __str_(self):
        return str(self.user_id) + " - " + str(self.payment_id) + " - " + str(self.payment_status)