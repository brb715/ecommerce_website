from re import template
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('signup/', views.sign_up, name='sign_up'),
    path('signin/', views.sign_in, name='sign_in'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('updatepassword/', views.update_password, name='password'),

    path('search/', views.search, name='search'),
    path('contact/', views.contact_us, name='contact_us'),
    path('about/', views.about, name='about'),

    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>/', views.mobile, name='mobiledata'),

    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>/', views.laptop, name='laptopdata'),

    path('bottomwear/', views.bottomwear, name='bottomwear'),
    path('bottomwear/<slug:data>', views.bottomwear, name='bottomweardata'),

    path('topwear/', views.topwear, name='topwear'),
    path('topwear/<slug:data>', views.topwear, name='topweardata'),

    path('product/<int:id>/', views.productdetail, name='productdetail'),

    path('addtocart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('pluscart/<int:pk>/', views.plus_cart, name='plus_cart'),
    path('minuscart/<int:pk>/', views.minus_cart, name='minus_cart'),
    path('remove/<int:pk>/', views.remove_item, name='remove_item'),

    path('order/', views.order_view, name='order_view'),
    path('checkout/', views.checkout_view, name='checkout_view')
]
