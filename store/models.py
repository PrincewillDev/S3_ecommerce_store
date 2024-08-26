from django.db import models
from enumfields import EnumField
from datetime import datetime
from .enum import Role, OrderStatus, PaymentStatus, PaymentMethod
import uuid

# Create your models here.
class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, max_length=100, unique=True)
    password = models.CharField(max_length=100, null=False, blank=False)
    role = EnumField(Role, max_length=30, null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return self.username + " - " + self.email + " - " + self.role.value

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

class inventory(models.Model):
    inventory_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return str(self.quantity) + " - " + str(self.product_id) + " - " + str(self.created_at)
    
class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    order_status = EnumField(OrderStatus, max_length=30, null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return str(self.order_id) + " - " + str(self.user_id) + " - " + str(self.created_at)
    

class OrderDetails(models.Model):
        order = models.ForeignKey(Order, on_delete=models.CASCADE)
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        quantity = models.IntegerField(null=False, blank=False)

        def __str__(self):
            return str(self.order.order_id) + " - " + str(self.product.product_name) + " - " + str(self.quantity)
class Payment(models.Model):
    payment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = EnumField(PaymentMethod, max_length=30, null=False, blank=False)
    payment_status = EnumField(PaymentStatus, max_length=30, null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return str(self.payment_id) + " - " + str(self.order_id) + " - " + str(self.payment_status) + " - " + str(self.created_at)
    
class invoices(models.Model):
    invoice_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    invoice_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    billing_details = models.TextField(max_length=225, null=False, blank=False)
    def __str__(self):
        return str(self.invoice_id) + " - " + str(self.payment_id) + " - " + str(self.invoice_amount) + " - " + str(self.created_at)
    
class cart(models.Model):
    cart_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
    added_at = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return str(self.cart_id) + " - " + str(self.user_id) + " - " + str(self.product_id) + " - " + str(self.quantity) + " - " + str(self.added_at)