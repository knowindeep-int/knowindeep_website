from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from bs4 import BeautifulSoup
import requests

from .models import Project,BlogTopics, Like, Comment

def topics(request):
    context = None
    if request.user.is_superuser:
        context = {
            "projects":Project.get_popular_projects()
        }
    else: 
        context = {
            "projects":Project.get_popular_approved_projects()
        }
    return render(request,"blogs/index.html",context)

def subtopics(request,slug):
    main_blog = Project.objects.get(slug=slug)
    blog = BlogTopics.objects.filter(link_to__slug=slug)
    context = {
        "blogs": blog,
        "blog_heading": slug,
        "main_blog":main_blog,
    }
    return render(request,"blogs/subtopic.html",context)

def blog_post(request,slug, blog):
    blog_content = BlogTopics.objects.get(slug=blog)
    all_blogs = BlogTopics.objects.filter(link_to__slug=slug)
    main_blog = Project.objects.get(slug=slug)
    author = blog_content.author
    # main_blog.increase_view
    # soup = BeautifulSoup(blog_content.content,"lxml")
    # for heading in soup.find_all(["h1", "h2", "h3"]):
    #     print(heading.name + ' ' + heading.text.strip())
    #     print(heading)
    # print(str(blog_content.get_next_blog) + str(blog_content.get_previous_blog))
    has_liked = blog_content.has_user_liked(request.user)
    context = {
        "main_blog":main_blog.title,
        "blog_content" : blog_content,
        "slug":slug,
        "all_blogs":all_blogs,
        "author": author,
        "has_liked": has_liked
    }
    return render(request,"blogs/blog_post.html", context)
    
def remove(request,slug):
    project = Project.objects.get(slug=slug)
    project.isApproved = False
    project.save()

    return redirect('blogs:index')


def approve(request,slug):
    project = Project.objects.get(slug=slug)
    project.isApproved = True
    project.save()

    return redirect('blogs:index')


def error404(request, exception):
    return HttpResponse("error")