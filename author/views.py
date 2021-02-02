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

    is_verified = profile.is_verified(user = request.user)
    packages = profile.getPackageProgressTuple

    context = {
        "profile": profile,
        "is_verified":is_verified,
        "progresses":packages
    }
    return render(request,"author/author_page.html",context)
    # return render(request, 'front-end/profile page/index.html', context)
 