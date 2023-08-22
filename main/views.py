from django.shortcuts import render, redirect
from .models import Category, SubCategory, Product, Cart
from .scrap import get_valute
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        val = request.POST.get('lezu')
        if val == 'hy': 
            usd = get_valute('USD')
            for i in Product.objects.filter():
                x = Product.objects.get(pk=i.id)
                x.price *= usd
                x.save()
            return redirect('index')
        elif val == 'ru':
            rub = get_valute('RUB')
            for i in Product.objects.filter():
                x = Product.objects.get(pk=i.id)
                x.price /= rub
                x.save()
            return redirect('index')
    category_list = Category.objects.all()
    all_product_list = Product.objects.all()
    sub_category_list = SubCategory.objects.all()
    return render(request, 'main/index.html', context={
        'category_list':category_list,
        'all_product_list':all_product_list,
        'sub_category_list':sub_category_list,
        'link':'index'
    })


def index_filter(request, id):
    category_list = Category.objects.all()
    prod_list = SubCategory.objects.filter(pk=id)
    sub_category_list = SubCategory.objects.all()
    return render(request, 'main/index_filter.html', context={
        'category_list':category_list,
        'prod_list':prod_list,
        'sub_category_list':sub_category_list,
        'link':'index_filter'

    })



def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={"register_form":form, 'link':'register'})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form, 'link':'login'})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")

def cart(request):
	cart_list = Cart.objects.all()
	return render(request, 'main/cart.html', context={
		'cart_list':cart_list,
        'link':'cart'
            
    })


def add_to_cart(request):
    if request.method == "POST":
        prod_id = request.POST.get('prod')
        my_prod = Product.objects.get(pk=prod_id)
        Cart.objects.create(prod=my_prod)
        return redirect('index')


def delete_to_cart(request):
    if request.method == "POST":
        prod_id = request.POST.get('prod')
        Cart.objects.filter(id=prod_id).delete()
        return redirect('cart')
