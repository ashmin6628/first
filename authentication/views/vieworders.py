from django.views import View
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password
from authentication.models import Product
from authentication.orders import Orders
from authentication.customer import Customer


class OrderView(View):
    
    def get(self , request ):
        customer = request.session.get('customer')
        orders = Orders.get_orders_by_customer(customer)
        orders = orders.reverse()
        return render(request , 'vieworders.html'  , {'orders' : orders})
