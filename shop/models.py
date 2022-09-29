from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    sub_category = models.CharField(max_length=20)
    desc = models.TextField()
    price = models.IntegerField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='shop/images')

    def __str__(self):
        return self.title


class Banner(models.Model):
    title = models.CharField(max_length=10)
    image = models.ImageField(upload_to='shop/images')

    def __str__(self):
        return self.title


class Change(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    new_password = models.CharField(max_length=50)

    def __str__(self):
        return self.user.first_name


class Contact(models.Model):
    name = models.CharField(max_length=20)
    phone_no = models.IntegerField()
    email = models.EmailField()
    issue = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return (f'Message from {self.name} - {self.email}')


class Checkout(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    current_address = models.CharField(max_length=200)
    permament_address = models.CharField(max_length=200)
    phone_no = models.IntegerField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.IntegerField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def __str__(self):
        return self.user.get_full_name

    def total_cost(self):
        return self.quantity*self.product.price


class Serie(models.Model):     # aka Order model
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'{self.user.first_name} - {self.product.title}') 
