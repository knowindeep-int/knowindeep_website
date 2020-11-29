from django.shortcuts import render
from django.http import HttpResponse

from blogs.models import Profile
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

    context = {
        "profile": profile,
        "is_verified":is_verified
    }
    return render(request,"author/author_page.html",context)
 