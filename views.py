from django.shortcuts import render, redirect
from .models import Shop, Product, Order, User
from .forms import SignUpForm, SignInForm
from django.contrib.auth import authenticate,login,logout

def home(request):
    shops = Shop.objects.all().order_by('-rating')[:5]
    current_user = request.user
    return render(request, 'home.html', {
        'shops': shops,
        'user': current_user,
    })

def shoplist(request):
    shops = Shop.objects.all()
    return render(request, 'shoplist.html', {
        'shops': shops,
    })

def shop_detail(request, shop_name):
    shop = Shop.objects.get(name=shop_name)
    products = Product.objects.filter(shop=shop)
    rating = shop.rating
    return render(request, 'shop.html', {
        'shop': shop,
        'products': products,
        'rating': rating,
    })

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    shop = Shop.objects.get(id=product.shop.id)
    products = Product.objects.filter(shop=shop)
    return render(request, 'product.html', {
        'product': product,
        'products': products,
    })

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = request.POST.get['email']
            password = request.POST.get['password']
            first_name = request.POST.get['first_name']
            last_name = request.POST.get['last_name']
            address = ""

            user = user(email=email, first_name=first_name, last_name=last_name, address=address, password=password)
            user.save()
            return redirect('/')
    else:
        return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = SignInForm()
    return render(request, 'login.html')

