from django.urls import path

from . import views

# Url-Patterns für unsere views
# Wurde connected mit der urls.py der root ecommerce directory

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('products/', views.products, name="products"),
   
    #added main path
    path("main", views.main, name="main"),
   
    #added login path
    path("login", views.login, name="login"),

    #added register path
    path("register", views.register_request, name="register")
]