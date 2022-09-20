from datetime import datetime
from django.db import models
from datetime import datetime


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


class Contact(models.Model):
    name = models.CharField(max_length=20)
    phone_no = models.IntegerField()
    email = models.EmailField()
    issue = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return (f'Message from {self.name} - {self.email}')
