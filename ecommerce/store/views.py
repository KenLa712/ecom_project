
#Views für unsere Seiten erstellt, indem die templates gerendert werden
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import NewUserForm
from .models import * 
from django.contrib import messages

def store(request):
     context = {}
     return render(request, 'store/store.html', context)

def cart(request):
     context = {}
     return render(request, 'store/cart.html', context)

def checkout(request):
      context = {}
      return render(request, 'store/checkout.html', context)
	  
def login(request):
      context = {}
      return render(request, 'store/login.html', context)

def main(request):
      context = {}
      return render(request, 'store/main.html', context)
      
def products(request):
      
      #data = cartData(request)
      #cartItems = data['cartItems']
      #order = data['order']
      #items = data['items']
      
      products = Produkt.objects.all()
      context = {'products':products}
      return render(request, 'store/products.html', context)


# Funktion um Registrierung durchzuführen
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, "Registration successful." )
			return redirect("register")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="store/register.html", context={"register_form":form})