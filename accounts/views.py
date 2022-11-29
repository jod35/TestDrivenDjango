from django.shortcuts import render
from .forms import UserRegistrationForm

# Create your views here.


def register_user(request):
    form = UserRegistrationForm()

    context = {'form':form}
    return render(request,'accounts/register.html',context)