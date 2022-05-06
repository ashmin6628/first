from django.contrib import admin
from django.urls import path, include
from . import views
from .views import home, signin, signup
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.vieworders import OrderView



urlpatterns = [
    path('', home.home.as_view(), name="home"),
    path('signup', signup.Signup.as_view(), name="signup"),
    path('signin', signin.Signin.as_view(), name="signin"),
    path('signout', home.signout, name="signout"),
    path('register', home.register, name="register"),
    path('order', home.Order.as_view(), name="order"),
    path('cart', Cart.as_view(), name="cart"),
    path('check-out', CheckOut.as_view(), name="check-out"),
    path('view', OrderView.as_view(), name="vieworder"),

]