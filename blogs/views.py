from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from bs4 import BeautifulSoup
import requests

from .models import Blog,BlogTopics, Like, Comment


def like_blog(request,slug,blog):
   try:
       like = Like.objects.get(user = request.user)
       like.delete()     
       return HttpResponseRedirect(reverse('blogs:blog_post',args=[blog,slug]))
   except Like.DoesNotExist:
        like = Like.objects.create(user=request.user, link_to=BlogTopics.objects.get(slug=slug))
        return HttpResponseRedirect(reverse('blogs:blog_post',args=[blog,slug]))
   

def topics(request):
    context = {
        "blogs":Blog.objects.all().order_by('-no_of_views')
    }
    return render(request,"blogs/index.html",context)

def subtopics(request,slug):
    main_blog = Blog.objects.get(slug=slug)
    main_blog.increase_view
    blog = BlogTopics.objects.filter(link_to__slug=slug)
    content = main_blog.topic_content[0:100] + "....."
    print(content)
    context = {
        "blogs": blog,
        "blog_heading": slug,
        "main_blog":main_blog,
        "content":content
    }
    return render(request,"blogs/subtopic.html",context)

def blog_post(request,slug, blog):
    blog_content = BlogTopics.objects.get(slug=blog)
    all_blogs = BlogTopics.objects.filter(link_to__slug=slug)
    main_blog = Blog.objects.get(slug=slug)
    author = blog_content.author
    # main_blog.increase_view
    # soup = BeautifulSoup(blog_content.content,"lxml")
    # for heading in soup.find_all(["h1", "h2", "h3"]):
    #     print(heading.name + ' ' + heading.text.strip())
    #     print(heading)
    has_liked = blog_content.has_user_liked(request.user)
    context = {
        "main_blog":main_blog.topic,
        "blog_content" : blog_content,
        "slug":slug,
        "all_blogs":all_blogs,
        "author": author,
        "has_liked": has_liked
    }
    return render(request,"blogs/blog_post.html", context)
    

def error404(request, exception):
    print("called 404")
    return HttpResponse("error")