from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, phone=None,password=None, **kwargs):
        kwargs.setdefault("is_active", True)
        kwargs.setdefault("is_staff", False)
        kwargs.setdefault("is_superuser", False)
        
        if not email:
            raise ValueError("Email bolishi shart")
        email = self.normalize_email(email=email)
        user = self.model(username=username,email=email, phone=phone, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    def create_superuser(self, email, username, phone, password, **kwargs):
        kwargs.setdefault("is_active", True)
        kwargs.setdefault("is_staff",True)
        kwargs.setdefault("is_superuser", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser bolishi uchun is_staff=True bolishi kerak")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser bolishi uchun is_superuser=True bolishi kerak")
            
        return self.create_user(email=email,username=username, phone=phone,password=password,**kwargs)
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username", "phone"]
    
    
    def __str__(self):
        return self.email
    
    