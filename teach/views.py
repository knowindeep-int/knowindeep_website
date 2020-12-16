from django.shortcuts import render, redirect
from django.http import HttpResponse

from blogs.models import Language, PreRequisite, Project, Profile

def add_course(request):
    if request.user.is_authenticated:
        languages = Language.getAllLanguages()
        pre_reqs = PreRequisite.getAllPreReqs()
        context = {
            'languages' : languages,
            'pre_reqs' : pre_reqs
        }
        return render(request, 'teach/new_course.html', context=context)
    print("45")
    return redirect("/")


def list_of_projects(request):
    user = request.user
    if user.is_authenticated:
        profile = Profile.objects.get(user=user)
        projects = profile.project_set.all()
        ongoing_projects = projects.filter(isCompleted=False)
        completed_projects = projects.filter(isCompleted=True)
        context = {
            'completed_projects': completed_projects,
            'ongoing_projects': ongoing_projects,
            }
        return render(request, 'teach/projects_list.html',context=context)
    return redirect("/")
