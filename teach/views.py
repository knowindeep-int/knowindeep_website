from django.shortcuts import render
from django.http import HttpResponse

def sample(request):
    return HttpResponse("URL IS BEING CALLED!")
# Create your views here.
