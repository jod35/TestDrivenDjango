from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.


def register_user(request):
    form = UserRegistrationForm()


    if request.method == "POST":
        form = UserRegistrationForm(request.POST)


        if form.is_valid():
            form.save()

            return redirect(reverse('login_page'))

    context = {'form':form}
    return render(request,'accounts/register.html',context)


def login_page(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)

                return redirect(reverse('homepage'))

    context ={
        'form':form
    }
    return render(request,"accounts/login.html",context)


def logout_user(request):
    logout(request)
    return redirect(reverse('homepage'))


