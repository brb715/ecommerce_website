from .models import Banner, Product, Contact, Cart, Serie, Checkout
from .forms import signup, signin, contact, checkout, profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q, F


def homepage(request):
    banners = Banner.objects.all()
    products = Product.objects.all()
    fashion = Product.objects.filter(category='Fashion')
    return render(request, 'shop/home.html', {'range': range(1, len(banners)), 'banner': banners, 'first_ban': banners[0], 'product': products, 'first_prod': products[0], 'fashion': fashion})


def mobile(request, data=None):
    if data == None:
        mobiles = Product.objects.filter(sub_category='Smartphones')
    elif data == 'below':
        mobiles = Product.objects.filter(Q(sub_category='Smartphones') & Q(price__lte=10000))
    elif data == 'above':
        mobiles = Product.objects.filter(Q(sub_category='Smartphones') & Q(price__gt=10000))
    else:
        mobiles = Product.objects.filter(Q(sub_category='Smartphones') & Q(title=data))
    return render(request, 'shop/smartphone.html', {'mobile': mobiles})


def topwear(request, data=None):
    if data == None:
        topwear = Product.objects.filter(sub_category='Top Wear')
    elif data == 'below':
        topwear = Product.objects.filter(Q(sub_category='Top Wear') & Q(price__lte=400))
    elif data == 'above':
        topwear = Product.objects.filter(Q(sub_category='Top Wear') & Q(price__gt=400))
    return render(request, 'shop/topwear.html', {'topwear': topwear})


def bottomwear(request, data=None):
    if data == None:
        bottomwear = Product.objects.filter(sub_category='Bottom Wear')
    elif data == 'below':
        bottomwear = Product.objects.filter(Q(sub_category='Bottom Wear') & Q(price__lte=600))
    elif data == 'above':
        bottomwear = Product.objects.filter(Q(sub_category='Bottom Wear') & Q(price__gt=600))
    return render(request, 'shop/bottomwear.html', {'bottomwear': bottomwear})


def laptop(request, data=None):
    if data == None:
        laptops = Product.objects.filter(sub_category='Laptops')
    elif data == 'below':
        laptops = Product.objects.filter(Q(sub_category='Laptops') & Q(price__lte=30000))
    elif data == 'above':
        laptops = Product.objects.filter(Q(sub_category='Laptops') & Q(price__gt=30000))
    else:
        laptops = Product.objects.filter(Q(sub_category='Laptops') & Q(title=data))
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

        fm = User.objects.create_user(username, email, password)
        fm.first_name = fname
        fm.last_name = lname
        fm.save()
        user = authenticate(username=username, password=password)
        login(request, user)
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
        else:
            messages.error(request, 'Credentials did not match with any records in our database')
            return redirect('sign_in')
    fm = signin()
    return render(request, 'shop/signin.html', {'form': fm})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('/')


@login_required
def update_password(request):
    current_user = request.user
    if request.method == 'POST':
        pass1 = request.POST['password']
        pass2 = request.POST['new_password']
        user = authenticate(username=current_user, password=pass1)
        if user is None:
            messages.error(request, 'Old Password do not match with the current password')
            return redirect('password')
        else:
            user = User.objects.get(username=current_user)
            user.set_password(pass2)
            user.save()
            messages.success(request, 'Password Updated')
            return redirect('/')
    return render(request, 'shop/change-password.html', {'username': current_user})


@login_required
def profile_view(request, pk):
    current_user = request.user
    fm = profile(instance=current_user)
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        User.objects.filter(id=pk).update(username=username, email=email, first_name=fname, last_name=lname)
        messages.success(request, 'Profile Updated')
        return redirect('/')
    return render(request, 'shop/profile.html', {'form': fm})


def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        ph_no = request.POST['phone_no']
        issue = request.POST['issue']
        fm = Contact(name=name, email=email, phone_no=ph_no, issue=issue)
        fm.save()
        messages.success(request, 'Successfully submitted the form')
        return redirect('/')
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


@login_required(login_url='sign_in')
def add_to_cart(request, pk):
    current_user = request.user
    if current_user.is_authenticated:
        product = Product.objects.get(id=pk)
        already_present = Cart.objects.filter(Q(user=current_user) & Q(product=product)).exists()
        if not already_present:
            Cart(user=current_user, product=product).save()
            messages.success(request, 'Product added to Cart')
        else:
            messages.info(request, 'Already added in cart')
    return redirect('cart')


@login_required(login_url='sign_in')
def cart(request):
    current_user = request.user
    all = Cart.objects.filter(user=current_user)
    total = 0.0
    for item in all:
        total = total+item.total_cost()
    return render(request, 'shop/cart.html', {'items': all, 'total': total, 'grand_total': (total+70.0)})


@login_required
def plus_cart(request, pk):
    current_user = request.user
    if current_user.is_authenticated:
        product = Product.objects.get(id=pk)
        item = Cart.objects.get(Q(user=current_user) & Q(product=product))
        item.quantity = F('quantity') + 1
        item.save()
    return redirect('cart')


@login_required
def minus_cart(request, pk):
    current_user = request.user
    if current_user.is_authenticated:
        product = Product.objects.get(id=pk)
        item = Cart.objects.get(Q(user=current_user) & Q(product=product))
        item.quantity = F('quantity') - 1
        item.save()
        if Cart.objects.get(Q(user=current_user) & Q(product=product)).quantity == 0:
            item.delete()
    return redirect('cart')


@login_required
def remove_item(request, pk):
    current_user = request.user
    product = Product.objects.get(id=pk)
    item = Cart.objects.get(Q(user=current_user) & Q(product=product))
    item.delete()
    messages.success(request, 'Successfully removed product from the cart.')
    return redirect('cart')


@login_required
def order_view(request):
    current_user = request.user
    orders = Serie.objects.filter(user=current_user)
    return render(request, 'shop/orders.html', {'products': orders})


@login_required
def checkout_view(request):
    current_user = request.user
    total = 0.0
    orders = Cart.objects.filter(user=current_user)
    for item in orders:
        total = total+item.total_cost()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        add1 = request.POST['current_address']
        add2 = request.POST['permament_address']
        pno = request.POST['phone_no']
        city = request.POST['city']
        state = request.POST['state']
        zcode = request.POST['zip_code']
        Checkout(name=name, email=email, current_address=add1, permament_address=add2, phone_no=pno, city=city, state=state, zip_code=zcode).save()

        list = [Serie(**item) for item in orders.values()]
        Serie.objects.bulk_create(list)
        Cart.objects.filter(user=current_user).delete()

        messages.success(request, 'Successfully Purchased')
        return redirect('order_view')
    fm = checkout()
    return render(request, 'shop/checkout.html', {'form': fm, 'items': orders, 'total': total, 'grand_total': total+70.0})


def about(request):
    return render(request, 'shop/about.html')
