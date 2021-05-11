from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from project.models import Language, Project, Profile,Chapter
from project.utils import getApiKey

import os

def add_course(request, pk = None):
    UNSPLASH_API_KEY_DEBUG,PEXELS_API_KEY_DEBUG ,IMGUR_CLIENT_ID_DEBUG,IMGUR_BEARER_DEBUG = getApiKey()  
    if request.user.is_authenticated:
        languages = Language.getAllLanguages()
        DEBUG = bool(int(os.environ.get('DEBUG') or 1 ))

        # pre_reqs = PreRequisite.getAllPreReqs()

        if pk is None:
            context = {
                'languages' : languages,        
                # 'pre_reqs' : pre_reqs,
                'IMGUR_CLIENT_ID_DEBUG': IMGUR_CLIENT_ID_DEBUG,
                'IMGUR_BEARER_DEBUG' : IMGUR_BEARER_DEBUG,
                'DEBUG':DEBUG
            }

        else:
            project  = Project.objects.get(pk = pk)
            status = Project.get_status(pk = pk)
            selected_languages = list(project.languages.all())
            #json.dumps(list(project.languages.all())
            overview = project.overview
            difficulty_level = project.difficulty_level
            
            context = {
                'languages': languages,
                # 'pre_reqs': pre_reqs,
                'project': project,
                'status': status,
                'overview': overview,
                'difficulty_level': difficulty_level,
                'selected_languages': selected_languages,
                'IMGUR_CLIENT_ID_DEBUG': IMGUR_CLIENT_ID_DEBUG,
                'IMGUR_BEARER_DEBUG' : IMGUR_BEARER_DEBUG,
                'DEBUG':DEBUG
            }
            
        print(context)
        # return render(request, 'teach/new_course.html', context=context)
        return render(request, "new/teach/new_course.html",context=context)
    return redirect("/")


def list_of_projects(request):
    user = request.user
    if user.is_authenticated:
        profile = Profile.getProfile(user)
        ongoing_projects, completed_projects = profile.getOngoingAndCompletedProjects
        context = {
            'completed_projects': completed_projects,
            'ongoing_projects': ongoing_projects,
        }
        return render(request, 'new/teach/new_project_list.html',context=context)
    return redirect("/")

def text_editor(request,pk = None, chapter_pk = None):
    UNSPLASH_API_KEY_DEBUG,PEXELS_API_KEY_DEBUG ,IMGUR_CLIENT_ID_DEBUG,IMGUR_BEARER_DEBUG = getApiKey()  
    if not chapter_pk:
        project = Project.objects.get(pk = pk)
        chapters = project.chapters.all()
        if chapter_pk is not None:
            chapter = Chapter.objects.get(pk = chapter_pk)
            context = {
            'chapters':chapters,
            'project': project,
            'chapter':chapter,
            'UNSPLASH_API_KEY_DEBUG':UNSPLASH_API_KEY_DEBUG,
            'PEXELS_API_KEY_DEBUG':PEXELS_API_KEY_DEBUG , 
            'IMGUR_CLIENT_ID_DEBUG': IMGUR_CLIENT_ID_DEBUG,
            'IMGUR_BEARER_DEBUG' : IMGUR_BEARER_DEBUG ,
            }
        print(project.slug)
        context = {
            'chapters':chapters,
            'project': project,
            'UNSPLASH_API_KEY_DEBUG':UNSPLASH_API_KEY_DEBUG,
            'PEXELS_API_KEY_DEBUG':PEXELS_API_KEY_DEBUG , 
            'IMGUR_CLIENT_ID_DEBUG': IMGUR_CLIENT_ID_DEBUG,
            'IMGUR_BEARER_DEBUG' : IMGUR_BEARER_DEBUG ,
            }
        

        return render(request, 'front-end/home page/teach.html',context=context)
    
    chapter = Chapter.objects.get(pk = chapter_pk)
    project = Project.objects.get(pk = pk)
    chapters = project.chapters.all()

    context = {
        'chapters': chapters,
        'chapter': chapter,
        'project': project,
        'UNSPLASH_API_KEY_DEBUG':UNSPLASH_API_KEY_DEBUG,
        'PEXELS_API_KEY_DEBUG':PEXELS_API_KEY_DEBUG , 
        'IMGUR_CLIENT_ID_DEBUG': IMGUR_CLIENT_ID_DEBUG,
        'IMGUR_BEARER_DEBUG' : IMGUR_BEARER_DEBUG ,
    }

    return render(request, 'front-end/home page/teach.html', context = context)

def delete(request, pk):
    Project.objects.get(pk = pk).delete()
    return redirect('teach:list_of_projects')