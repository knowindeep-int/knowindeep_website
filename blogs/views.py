from django.shortcuts import render

from .models import Blog,BlogTopics

def topics(request):
    context = {
        "blogs":Blog.objects.all()
    }
    return render(request,"blogs/index.html",context)

def subtopics(request,slug):
    context = {
        "blogs": BlogTopics.objects.filter(link_to__slug=slug)
    }
    return render(request,"blogs/subtopic.html",context)

def blog_post(request,slug, blog):
    blog_content = BlogTopics.objects.filter(slug=blog)
    context = {
        "blog_content" : blog_content
    }
    return render(request,"blogs/blog_post.html", context)
    