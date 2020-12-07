from django.shortcuts import render
from django.http import HttpResponse

from blogs.models import Language

def add_course(request):
    if request.user.is_authenticated:
        languages = Language.getAllLanguages()
        context = {
            'languages': languages
        }
        return render(request, 'teach/new_course.html', context=context)
    
    raise Exception("You are not Authorized to access this page")
    #return HttpResponse("You are not Authorized to access this page", status = 500)
# Create your views here.
