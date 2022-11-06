from django.contrib import admin
from .models import Banner, Product, Contact, Checkout, Cart, Serie


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'pub_date', 'price')
    exclude = ('pub_date',)


admin.site.register(Banner)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact)
admin.site.register(Checkout)
admin.site.register(Cart)
admin.site.register(Serie)