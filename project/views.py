from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
import requests
import sys

import os
from .models import Project,Chapter, Like, Comment
from blogs.models import Blog

def topics(request):
    context = None
    if request.user.is_superuser:
        context = {
            "projects":Project.get_popular_projects(),
            "all_projects" : Project.get_all_projects(),
            'blogs': Blog.objects.filter(isCompleted = True)
        }
    else: 
        context = {
            "projects":Project.get_popular_approved_completed_projects(),
            "all_projects" : Project.get_all_approved_projects(),
            'blogs':Blog.objects.filter(isApproved = True, isCompleted = True)
        }
    print(request)
    return render(request,"new/blogs/new_index.html",context)

def subtopics(request,slug):
    project = Project.objects.get(slug=slug)
    if project.canUserView(request.user):
        #blog = Chapter.objects.filter(link_to__slug=slug)
        chapters = Project.getAllChapters(slug)
        has_liked = project.has_user_liked(request.user)

        context = {
            "chapters": chapters,
            "chapter_heading": slug,
            "project":project,
            "has_liked": has_liked,
            "can_review": False
        }
        return render(request,"new/blogs/new_project_page.html",context)
    return HttpResponse('You are not allowed to access this page', status =500)

def chapter_post(request,slug, chapter):
    project = Project.objects.get(slug = slug)
    if project.canUserView(request.user):
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
        # has_liked = chapter_content.has_user_liked(request.user)
        context = {
            "title":title,
            "chapter_content" : chapter_content,
            "slug":slug,
            "chapters":chapters,
            "author": author,
            "can_review": False
            # "has_liked": has_liked
        }
        return render(request,"new/blogs/new_chapter_page.html", context)
    return HttpResponse('You are not allowed to access this page', status =500)

def remove(request,slug,method):
    
    if request.user.is_superuser and method=='project':
        project = Project.objects.get(slug=slug)
        project.isApproved = False
        project.save()

        return redirect('project:index')
    if request.user.is_superuser and method=='blog':
        project = Blog.objects.get(slug=slug)
        project.isApproved = False
        project.save()

        return redirect('project:index')
    return HttpResponse("You are not Authorized to access this Page", status = 500)

def approve(request,slug,method):
    if request.user.is_superuser and method=='project':
        project = Project.objects.get(slug=slug)
        project.approveProject
        return redirect('project:index')
    if request.user.is_superuser and method=='blog':
        project = Blog.objects.get(slug=slug)
        project.isApproved = True
        project.save()
        return redirect('project:index')
    return HttpResponse("You are not Authorized to access this Page", status = 500)

# def list_all_blogs(request):
#     context = {'blogs':Blog.objects.all()}
#     return render(request,'blogs/list_all_blogs.html',context)

def review_subtopics(request,slug):
    project = Project.objects.get(slug=slug)
    # print(project.canUserReview(request.user))
    if project.canUserView(request.user) or  project.canUserReview(request.user):
        #blog = Chapter.objects.filter(link_to__slug=slug)
        chapters = Project.getAllChapters(slug)
        has_liked = project.has_user_liked(request.user)

        context = {
            "chapters": chapters,
            "chapter_heading": slug,
            "project":project,
            "has_liked": has_liked,
            "can_review": True
        }
        return render(request,"new/blogs/new_project_page.html",context)
    return HttpResponse('You are not allowed to access this page', status =500)


def chapter_post_review(request,slug, chapter):
    project = Project.objects.get(slug = slug)
    if project.canUserView(request.user) or project.canUserReview(request.user):
        chapter_content = Chapter.objects.get(slug=chapter)
        #all_blogs = Chapter.objects.filter(link_to__slug=slug)
        chapters = Project.getAllChapters(slug)
        #main_blog = Project.objects.get(slug=slug)
        title = Project.getTitle(slug = slug)
        author = chapter_content.author
        context = {
            "title":title,
            "chapter_content" : chapter_content,
            "slug":slug,
            "chapters":chapters,
            "author": author,
            "can_review": True
        }
        return render(request,"new/blogs/new_chapter_page.html", context)
    return HttpResponse('You are not allowed to access this page', status =500)

def error404(request, exception):
    return HttpResponse(request)

def error400(request, exception):
    return HttpResponse("error400")

def error500(request):
    type_, value, traceback = sys.exc_info()
    return HttpResponse(value)

