from django.views import View
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from authentication.models import Customer


class Signin(View):
    return_url = None
    def get(self , request):
        Signin.return_url = request.GET.get('return_url')
        return render(request, "authentication/signin.html")

    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password , customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Signin.return_url:
                    return HttpResponseRedirect(Signin.return_url)
                else:
                    Signin.return_url = None
                    return redirect('home')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'
        print(email,password)       
        return render(request , 'authentication/signin.html' ,{'error' : error_message})

def signout(request):
    request.session.clear()
    return redirect('signin')