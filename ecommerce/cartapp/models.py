from django.db import models
from ecomapp.models import product
# Create your models here.
class Cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    date_added=models.DateField(auto_now=True)

    class Meta:
        db_table='Cart'
        ordering=['date_added']
    def __str__(self):
        return '{}'.format(self.cart_id)

class Cart_item(models.Model):
    Product=models.ForeignKey(product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='Cart_item'

    def sub_total(self):
        return self.Product.price * self.quantity

    def __str__(self):
        return '{}'.format(self.Product)

class Caarrt_item(models.Model):
    Product=models.ForeignKey(product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='Caarrt_item'

    def sub_total(self):
        return self.Product.price * self.quantity

    def __str__(self):
        return '{}'.format(self.Product)