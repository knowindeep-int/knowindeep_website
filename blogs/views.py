from django.shortcuts import render
from .models import Blog
# Create your views here.
def blogs(request,slug):
    blog= Blog.objects.get(slug=slug)
    context = {'blog':blog}
    return render(request,'new/topics/blog.html',context=context)