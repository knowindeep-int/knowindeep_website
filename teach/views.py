from django.shortcuts import render, redirect
from django.http import HttpResponse

from blogs.models import Language, PreRequisite, Project, Profile

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
            
            context = {
                'languages': languages,
                'pre_reqs': pre_reqs,
                'project': project,
                'status': status
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
