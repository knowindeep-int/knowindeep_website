from django.shortcuts import render
from django.http import HttpResponse

from blogs.models import Language, PreRequisite

def add_course(request):
    if request.user.is_authenticated:
        languages = Language.getAllLanguages()
        pre_reqs = PreRequisite.getAllPreReqs()
        context = {
            'languages' : languages,
            'pre_reqs' : pre_reqs
        }
        return render(request, 'teach/new_course.html', context=context)
    
    raise Exception("You are not Authorized to access this page")
    #return HttpResponse("You are not Authorized to access this page", status = 500)
# Create your views here.
