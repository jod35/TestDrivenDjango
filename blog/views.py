from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry

# Create your views here.

def homepage(request):
    entries = Entry.objects.all()

    return render(request,'blog/index.html',{"entries":entries})


def detail_page(request,id):
    return render(request,"blog/detail.html")
    