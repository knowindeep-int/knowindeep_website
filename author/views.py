from django.shortcuts import render
from django.http import HttpResponse

def author_page(request, slug):
    return render(request,"author/author_page.html",{})