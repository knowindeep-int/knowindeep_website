from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from django.core.validators import ValidationError

from .models import Todo

def index(request):
    todo_items = Todo.objects.all().order_by('-added_date')
    return render(request,"to_do_app/index.html",{"todo_items":todo_items})

def add_todo(request):
    print(request)
    added_date = timezone.now()
    content = request.POST["content"]
    if content == "" or None:
        return redirect("/")
    Todo.objects.create(added_date=added_date,text=content)
    return redirect("/")

def delete_todo(request,pk):
    Todo.objects.get(pk=pk).delete()
    return redirect("/")