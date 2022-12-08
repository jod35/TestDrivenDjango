from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.urls import reverse


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
    return render(request,"accounts/login.html")