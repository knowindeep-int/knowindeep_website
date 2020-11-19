from django.shortcuts import render
from django.http import HttpResponse

def add_course(request):
    return render(request, 'teach/new_course.html', context={})
# Create your views here.
