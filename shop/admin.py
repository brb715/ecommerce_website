from django.contrib import admin
from .models import Banner,Product, Contact, Checkout, Cart

# Register your models here.
admin.site.register(Banner)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Checkout)
admin.site.register(Cart)