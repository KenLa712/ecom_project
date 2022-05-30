from multiprocessing import context
from django.shortcuts import render
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from .models import * 

#Views für unsere Seiten erstellt, indem die templates gerendert werden

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



# Funktion um Registrierung durchzuführen
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("store:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="store/register.html", context={"register_form":form})