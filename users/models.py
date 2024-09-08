from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from datetime import datetime
import uuid
from .manager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length=100, verbose_name=('First Name'))
    lastname = models.CharField(max_length=100, verbose_name=('Last Name'))
    email = models.EmailField(null=False, blank=False, max_length=100, unique=True)
    contact_no = models.CharField(null=False, blank=False, max_length=80)
    password = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)  

    objects = UserManager()

    USERNAME_FIELD = 'email'  # Email as the primary identifier
    REQUIRED_FIELDS = ['firstname', 'lastname', 'contact_no', 'password']

    def __str__(self):
        return f"{self.email}"
    
    @property
    def get_full_name(self):
        return f"{self.firstname} {self.lastname}"
    
class OneTimePassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # OneToOne relationship with User    
    code = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return f'{self.user.firstname} --passcode'

