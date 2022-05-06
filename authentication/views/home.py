from django.shortcuts import redirect, render, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from authentication import orders
from authentication.models import Contact, RestaurentRegister, Product, Category
from django.views import View


# Create your views here.
class home(View):
    def get(self , request):
        return render(request, "index.html")

    def post(self , request):
        name = request.POST.get('c_name')
        email = request.POST.get('c_email')
        message = request.POST.get('c_message')

        contact = Contact(name=name, email=email, message=message)
        contact.save()

        return render(request, "index.html")



   

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')



#####################################################

def register(request):
    if request.method == "POST":
        name = request.POST['r_name']
        address = request.POST['r_address']
        contact = request.POST['r_contact']

        register = RestaurentRegister(name=name, address=address, contact=contact)
        register.save()

    return render(request, "register.html")


############################################################

class Order(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:  
                if remove:   
                    if quantity <= 1:
                        cart.pop(product)   
                    else:
                        cart[product] = quantity - 1
                else:
                   cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart ={}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('home')


    def get(self , request):   
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None        
        categories = Category.get_all_categories();
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products();

        data = {}
        data['products'] = products
        data['categories'] = categories
         
        print('you are :' , request.session.get('email'))
        return render(request, 'order.html', data)
        

#######
