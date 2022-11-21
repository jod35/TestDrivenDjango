from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "posts/index.html",{"posts":posts})


def post_detail(request,id):
    post =  Post.objects.get(id=id)
    context = {
        'post':post,
        'title':post.title
    }
    return render(request,'posts/detail.html',context)