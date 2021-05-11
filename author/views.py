from django.shortcuts import render,redirect
from django.http import HttpResponse

from project.models import Profile, Package, Progress
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from project.models import myUser

from project.utils import getApiKey


def author_page(request, slug):
    UNSPLASH_API_KEY_DEBUG,PEXELS_API_KEY_DEBUG ,IMGUR_CLIENT_ID_DEBUG,IMGUR_BEARER_DEBUG = getApiKey()  

    if slug == "@me":
        user = request.user
    else:
        user = myUser.objects.get(email=slug)

    context = None

    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = None

    is_verified = profile.is_verified(user = request.user)
    packages = profile.getPackageProgressTuple

    context = {
        "profile": profile,
        "is_verified":is_verified,
        "progresses":packages,
        'IMGUR_CLIENT_ID_DEBUG': IMGUR_CLIENT_ID_DEBUG,
        'IMGUR_BEARER_DEBUG' : IMGUR_BEARER_DEBUG
    }
    return render(request,"new/author/new_author.html",context)
    # return render(request, 'front-end/profile page/index.html', context)

def delete(request):
    profile = Profile.objects.get(user = request.user)
    profile.user.delete()
    profile.delete()
    return redirect('project:index')
 

