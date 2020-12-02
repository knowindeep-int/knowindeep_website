from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from bs4 import BeautifulSoup
import requests
import sys

from .models import Project,Chapter, Like, Comment

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
    project = Project.objects.get(slug=slug)
    #blog = Chapter.objects.filter(link_to__slug=slug)
    chapters = Project.getAllChapters(slug)
    context = {
        "chapters": chapters,
        "chapter_heading": slug,
        "project":project,
    }
    return render(request,"blogs/subtopic.html",context)

def chapter_post(request,slug, chapter):
    chapter_content = Chapter.objects.get(slug=chapter)
    #all_blogs = Chapter.objects.filter(link_to__slug=slug)
    chapters = Project.getAllChapters(slug)
    #main_blog = Project.objects.get(slug=slug)
    title = Project.getTitle(slug = slug)
    author = chapter_content.author
    # main_blog.increase_view
    # soup = BeautifulSoup(blog_content.content,"lxml")
    # for heading in soup.find_all(["h1", "h2", "h3"]):
    #     print(heading.name + ' ' + heading.text.strip())
    #     print(heading)
    # print(str(blog_content.get_next_blog) + str(blog_content.get_previous_blog))
    has_liked = chapter_content.has_user_liked(request.user)
    context = {
        "title":title,
        "chapter_content" : chapter_content,
        "slug":slug,
        "chapters":chapters,
        "author": author,
        "has_liked": has_liked
    }
    return render(request,"blogs/blog_post.html", context)


def remove(request,slug):
    if request.user.is_superuser:
        project = Project.objects.get(slug=slug)
        project.isApproved = False
        project.save()

        return redirect('blogs:index')
    return HttpResponse("You are not Authorized to access this Page", status = 500)

def approve(request,slug):
    if request.user.is_superuser:
        project = Project.objects.get(slug=slug)
        project.isApproved = True
        project.save()

        return redirect('blogs:index')
    return HttpResponse("You are not Authorized to access this Page", status = 500)


def error404(request, exception):
    return HttpResponse("error404")

def error400(request, exception):
    return HttpResponse("error400")

def error500(request):
    type_, value, traceback = sys.exc_info()
    return HttpResponse(value)