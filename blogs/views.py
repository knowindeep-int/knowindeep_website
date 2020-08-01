from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Blog,BlogTopics

def topics(request):
    context = {
        "blogs":Blog.objects.all()
    }
    return render(request,"blogs/index.html",context)

def subtopics(request,slug):
    blog = BlogTopics.objects.filter(link_to__slug=slug)
    print(blog)
    context = {
        "blogs": blog,
        "blog_heading": slug
    }
    return render(request,"blogs/subtopic.html",context)

def blog_post(request,slug, blog):
    blog_content = BlogTopics.objects.filter(slug=blog)
    context = {
        "blog_content" : blog_content
    }
    return render(request,"blogs/blog_post.html", context)
    