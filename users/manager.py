from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email

class UserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError as e:
            raise ValueError(_("Invalid email address"))
    
    def create_user(self, email, firstname, lastname, password, **extra_fields):
        if email:
            email=self.normalize_email(email)
            self.email_validator(email)

        else:
            raise ValueError(_("The Email field must be set"))
        
        if not firstname:
            raise ValueError(_("First Name is required"))
        if not lastname:
            raise ValueError(_("Last Name is required"))
        user=self.model(email=email, firstname=firstname, lastname=lastname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, firstname, lastname, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_verified', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=True"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))
        
        user=self.create_user(email, firstname, lastname, password, **extra_fields)
        user.save(using=self._db)
        return self.create_user(email, firstname, lastname, password, **extra_fields)