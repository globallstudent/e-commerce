from django.db import models

from common.models import BaseModel
from common.choices import OrderStatus

class Order(BaseModel):
    user = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True)
    total_price = models.BigIntegerField(null=False, blank=False)
    status = models.CharField(choices=OrderStatus.choices, blank=False, null=False)
    notes = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username if self.user else 'Guest'} - {self.status}"


class OrderItem(BaseModel):
    order = models.ForeignKey('orders.Order', on_delete=models.RESTRICT, related_name='items')
    product = models.ForeignKey('products.ProductVariant', on_delete=models.RESTRICT, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=False, blank=False)
    price = models.BigIntegerField(null=False, blank=False)

    def __str__(self):
        return f"OrderItem {self.id} - {self.product.name if self.product else 'Unknown'} - {self.quantity} - {self.price}"

    
