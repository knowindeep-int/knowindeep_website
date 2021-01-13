from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from blogs.models import Language, PreRequisite, Project, Profile,Chapter,getApiKey

def add_course(request, pk = None):
    if request.user.is_authenticated:
        languages = Language.getAllLanguages()
        pre_reqs = PreRequisite.getAllPreReqs()

        if pk is None:
            context = {
                'languages' : languages,        
                'pre_reqs' : pre_reqs
            }

        else:
            project  = Project.objects.get(pk = pk)
            status = Project.get_status(pk = pk)
            selected_languages = list(project.languages.all())
            #json.dumps(list(project.languages.all())
            overview = project.overview
            difficulty_level = project.difficulty_level
            no_of_hours = project.no_of_hours
            context = {
                'languages': languages,
                'pre_reqs': pre_reqs,
                'project': project,
                'status': status,
                'overview': overview,
                'difficulty_level': difficulty_level,
                'no_of_hours': no_of_hours,
                'selected_languages': selected_languages
            }
            
        return render(request, 'teach/new_course.html', context=context)
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
        return render(request, 'teach/projects_list.html',context=context)
    return redirect("/")

def text_editor(request,pk = None, chapter_pk = None):
    UNSPLASH_API_KEY,PEXELS_API_KEY ,IMGUR_CLIENT_ID,IMGUR_BEARER = getApiKey()  
    if not chapter_pk:
        project = Project.objects.get(pk = pk)
        chapters = project.chapters.all()
        print(project.slug)
        context = {
            'chapters':chapters,
            'project': project,
            'UNSPLASH_API_KEY':UNSPLASH_API_KEY,
            'PEXELS_API_KEY':PEXELS_API_KEY , 
            'IMGUR_CLIENT_ID': IMGUR_CLIENT_ID,
            'IMGUR_BEARER' : IMGUR_BEARER ,
            }

        return render(request, 'front-end/home page/teach.html',context=context)
    
    chapter = Chapter.objects.get(pk = chapter_pk)
    project = Project.objects.get(pk = pk)
    chapters = project.chapters.all()

    context = {
        'chapters': chapters,
        'chapter': chapter,
        'project': project,
        'UNSPLASH_API_KEY':UNSPLASH_API_KEY,
        'PEXELS_API_KEY':PEXELS_API_KEY , 
        'IMGUR_CLIENT_ID': IMGUR_CLIENT_ID,
        'IMGUR_BEARER' : IMGUR_BEARER ,
    }

    return render(request, 'front-end/home page/teach.html', context = context)