from django.shortcuts import render
from django.http import HttpResponse

from blogs.models import Profile

def author_page(request, slug):
    context = None
    profile = Profile.objects.all()[0]
    context = {
        "profile": profile
    }
    return render(request,"author/author_page.html",context)