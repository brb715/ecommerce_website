from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Banner, Product, Contact
from .forms import signup, signin, contact


def homepage(request):
    banners = Banner.objects.all()
    products = Product.objects.all()
    fashion = Product.objects.filter(category='Fashion')
    return render(request, 'shop/home.html', {'range': range(1, len(banners)), 'banner': banners, 'first_ban': banners[0], 'product': products, 'first_prod': products[0], 'fashion': fashion})


def mobile(request, data=None):
    if data == None:
        mobiles = Product.objects.filter(sub_category='Smartphones')
    elif data == 'below':
        mobiles = Product.objects.filter(
            sub_category='Smartphones').filter(price__lte=10000)
    elif data == 'above':
        mobiles = Product.objects.filter(
            sub_category='Smartphones').filter(price__gt=10000)
    else:
        mobiles = Product.objects.filter(
            sub_category='Smartphones').filter(title=data)
    return render(request, 'shop/smartphone.html', {'mobile': mobiles})


def topwear(request, data=None):
    if data == None:
        topwear = Product.objects.filter(sub_category='Top Wear')
    elif data == 'below':
        topwear = Product.objects.filter(
            sub_category='Top Wear').filter(price__lte=400)
    elif data == 'above':
        topwear = Product.objects.filter(
            sub_category='Top Wear').filter(price__gt=400)
    return render(request, 'shop/topwear.html', {'topwear': topwear})


def bottomwear(request, data=None):
    if data == None:
        bottomwear = Product.objects.filter(sub_category='Bottom Wear')
    elif data == 'below':
        bottomwear = Product.objects.filter(
            sub_category='Bottom Wear').filter(price__lte=600)
    elif data == 'above':
        bottomwear = Product.objects.filter(
            sub_category='Bottom Wear').filter(price__gt=600)
    return render(request, 'shop/bottomwear.html', {'bottomwear': bottomwear})


def laptop(request, data=None):
    if data == None:
        laptops = Product.objects.filter(sub_category='Laptops')
    elif data == 'below':
        laptops = Product.objects.filter(
            sub_category='Laptops').filter(price__lte=30000)
    elif data == 'above':
        laptops = Product.objects.filter(
            sub_category='Laptops').filter(price__gt=30000)
    else:
        laptops = Product.objects.filter(
            sub_category='Laptops').filter(title=data)
    return render(request, 'shop/laptop.html', {'laptop': laptops})


def productdetail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'shop/productdetail.html', {'product': product})


def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        if not username.isalnum():
            messages.error(request, 'Username should not contain characters')
            return redirect('/')

        fm = User.objects.create_user(username, email, password)
        fm.first_name = fname
        fm.last_name = lname
        fm.save()
        messages.success(request, 'You successfully signed up for the website')
        return redirect('/')
    fm = signup()
    return render(request, 'shop/signup.html', {'form': fm})


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Logged In')
            return redirect('/')
    fm = signin()
    return render(request, 'shop/signin.html', {'form': fm})


def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('/')


def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        ph_no = request.POST['phone_no']
        issue = request.POST['issue']
        fm = Contact(name=name, email=email, phone_no=ph_no, issue=issue)
        fm.save()
        messages.success(request, 'Successfully submitted the form')
    fm = contact()
    return render(request, 'shop/contact.html', {'form': fm})


def search(request):
    query = request.GET['search']
    if len(query) > 78 or len(query) == 0:
        all = Product.objects.none()
    else:
        alltitle = Product.objects.filter(title__icontains=query)
        alldesc = Product.objects.filter(desc__icontains=query)
        allsub_category = Product.objects.filter(sub_category__icontains=query)
        all = alltitle.union(alldesc.union(allsub_category))
    return render(request, 'shop/search.html', {'allSearches': all, 'query': query})


def cart(request):
    return render(request, 'shop/cart.html')
