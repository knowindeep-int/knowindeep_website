from django.shortcuts import render
from django.http import HttpResponse

from blogs.models import Profile
from django.forms.models import model_to_dict

def author_page(request, slug):
    context = None
    try:
        profile = Profile.objects.get(name=slug)
    except Profile.DoesNotExist:
        profile = None

    context = {
        "profile": profile
    }
    return render(request,"author/author_page.html",context)