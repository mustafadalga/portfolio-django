from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.

# Create your views here.

def blogs(request):
    blogs=Blog.objects.all
    context={
        'blogs':blogs
    }
    return render(request,'blog/blog.html',context)

def detay(request,id):
    detay=get_object_or_404(Blog,pk=id)
    context={
        'detay':detay
    }
    return render(request,'blog/detay.html',context)