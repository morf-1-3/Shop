from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile
# Create your views here.
from django.db import IntegrityError
from django.http import HttpRequest


def loggout_view(request: HttpRequest):
    logout(request)
    return redirect('product')

def register(request: HttpRequest):
    context ={}
    # if request.user.is_authenticated:
        # return redirect('catalog:product')
    if request.method == "POST":
        
        first_name = request.POST.get("firstname")
        if first_name:
            first_name = first_name.capitalize()
        last_name = request.POST.get("lastname")
        if last_name:
            last_name = last_name.capitalize()
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone_number = request.POST.get("phone_number")
        context["first_name"] = first_name
        context["last_name"] = last_name
        context["username"] = username
        context["phone_number"] = phone_number
        if first_name and last_name and username and email and password and phone_number:
            try:
                
                new_user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                UserProfile.objects.create(phone_number=phone_number, user=new_user)


                return redirect("login")
            except IntegrityError:
                context['error'] = "Логін вже існує"
        else:
            context['error'] = "Заповніть всі поля"
    return render(request,'users/register.html',context)
    

def auth(request: HttpRequest):
    context = {}

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if username and password:
            user = authenticate(username = username, password = password)
            
            if user:
                login(request,user)
                return redirect('product')
            else:
                context["error"] = "Неправильно логін або пароль"
        else:
            context["error"] = "Заповніть всі поля"
    
    return render(request,"users/auth.html",context)



