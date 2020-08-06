from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
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
    main_blog.increase_view()
    main_blog.save()
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
    comments = Comment.objects.filter(link_to=blog_content)
    main_blog.increase_view()
    main_blog.save()
    context = {
        "main_blog":main_blog.topic,
        "blog_content" : blog_content,
        "slug":slug,
        "all_blogs":all_blogs,
        "comments":comments,
    }
    return render(request,"blogs/blog_post.html", context)
    

def error404(request, exception):
    print("called 404")
    return HttpResponse("error")