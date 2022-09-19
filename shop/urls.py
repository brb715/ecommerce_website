from re import template
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.homepage, name='home'),
    path('signup/', views.sign_up, name='sign_up'),
    path('signin/', views.sign_in, name='sign_in'),
    path('logout/', views.logout_view, name='logout'),

    path('search/', views.search, name='search'),

    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>/', views.mobile, name='mobiledata'),

    # path('laptop/', views.laptop, name='laptop'),
    # path('laptop/<slug:data>/', views.laptop, name='laptopdata'),

    path('bottomwear/', views.bottomwear, name='bottomwear'),
    path('bottomwear/<slug:data>', views.bottomwear, name='bottomweardata'),

    path('topwear/', views.topwear, name='topwear'),
    path('topwear/<slug:data>', views.topwear, name='topweardata'),

    path('product/<int:id>/', views.productdetail, name='productdetail'),

    path('cart/', views.cart, name='cart'),
]
