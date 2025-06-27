from django.db import models

from common.models import BaseModel

class Product(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    price = models.BigIntegerField(null=False, blank=False)
    brand = models.ForeignKey('products.Brand', on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=False)
    default_images = models.ManyToManyField('common.MediaFile',     blank=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey('products.Category', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    

class ProductVariant(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    price = models.BigIntegerField(null=False, blank=False)
    product = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True, blank=True)
    images = models.ManyToManyField('common.MediaFile', blank=True)
    stock = models.IntegerField(default=0, null=False, blank=False)
    size = models.ForeignKey('products.Size', on_delete=models.SET_NULL, null=True, blank=True)
    color = models.ForeignKey('products.Color', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.name}"
    

class Brand(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=False)
    logo = models.ImageField(upload_to='brands/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Category(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name

class Size(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name
    
class Color(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name
