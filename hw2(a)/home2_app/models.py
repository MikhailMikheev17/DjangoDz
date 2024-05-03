from django.db import models
from datetime import date

class Client(models.Model):     
    name = models.CharField(max_length=100)        
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_of_registration = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'User name: {self.name}, email:{self.email}, phone: {self.phone}, address: {self.address}, ' \
               f'date_registration: {self.date_of_registration}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2) 
    description = models.TextField()                            
    quantity_of_goods = models.IntegerField(default=0)
    product_update_date = models.DateTimeField(date)


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE) 
    products = models.ManyToManyField(Product)                   
    date_ordered = models.DateTimeField(auto_now_add=True)       
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

