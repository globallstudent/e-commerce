from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from common.models import BaseModel
from accounts.manager import UserManager

class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(unique=True, verbose_name="Email Address")
    password = models.CharField(max_length=128, verbose_name="Password")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone Number")
    first_name = models.CharField(max_length=30, blank=True, null=True, verbose_name="First Name")
    last_name = models.CharField(max_length=30, blank=True, null=True, verbose_name="Last Name")
    bio = models.TextField(blank=True, null=True, verbose_name="Bio")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="Avatar")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    is_staff = models.BooleanField(default=False, verbose_name="Is Staff")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    

class Cart(BaseModel):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user
    
class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.RESTRICT, null=True, blank=True)
    product = models.ForeignKey('products.ProductVariant', on_delete=models.RESTRICT, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=False, blank=False)
