from django.contrib import admin
from django.urls import path, include
from . import views
from .views import signin, signup
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.vieworders import OrderView
from .middlewares.auth import  auth_middleware
from .views.home import home, Order, signout, register



urlpatterns = [
    path('', home.as_view(), name="home"),
    path('signup', signup.Signup.as_view(), name="signup"),
    path('signin', signin.Signin.as_view(), name="signin"),
    path('signout', signout, name="signout"),
    path('register', register, name="register"),
    path('order', Order.as_view(), name="order"),
    path('cart', Cart.as_view(), name="cart"),
    path('check-out', CheckOut.as_view(), name="check-out"),
    path('view', auth_middleware(OrderView.as_view()), name="vieworder"),
    
]