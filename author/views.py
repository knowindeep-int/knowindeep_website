from django.shortcuts import render
from django.http import HttpResponse

from blogs.models import Profile, Package, Progress
from django.forms.models import model_to_dict
from django.contrib.auth.models import User

def author_page(request, slug):
    if slug == "me":
        user = request.user
    else:
        user = User.objects.get(username=slug)

    context = None

    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = None

    is_verified = request.user == profile.user
    packages = Package.objects.filter(profile = profile)
    #print(packages[0].project)
    percent_progress = []
    for i in range(packages.count()):
        percent_progress.append(packages[i].progress_set.all().count() / packages[i].project.chapter_set.all().count() * 100 ) 
    print(percent_progress)
    print(tuple(zip(packages, percent_progress)))
    context = {
        "profile": profile,
        "is_verified":is_verified,
        #"packages" : packages,
        #"percent_progress" : percent_progress
        "progresses":tuple(zip(packages, percent_progress))
    }
    return render(request,"author/author_page.html",context)
 