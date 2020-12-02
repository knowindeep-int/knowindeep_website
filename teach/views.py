from django.shortcuts import render
from django.http import HttpResponse

def add_course(request):
    if request.user.is_authenticated:
        return render(request, 'teach/new_course.html', context={})
    
    raise Exception("You are not Authorized to access this page")
    #return HttpResponse("You are not Authorized to access this page", status = 500)
# Create your views here.
