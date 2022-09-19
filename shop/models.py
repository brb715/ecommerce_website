from django.db import models

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