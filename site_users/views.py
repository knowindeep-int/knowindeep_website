from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import json

def login_page(request):
    error = None

    if request.user.is_authenticated:
        return redirect(reverse('project:index'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(reverse('project:index'))
        else:
            error = "Username or password is incorrect"

    context = {
        "error":error
    }

    return render(request,"site_users/login.html",context)

def logout_user(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))

def register_page(request):

    if request.user.is_authenticated:
        return redirect(reverse('project:index'))

    form = CreateUserForm()
    errors = None

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('site_users:login'))
        else:
            data = form.errors
            errors = json.dumps(data.as_json.__self__)
            errors_list = list(json.loads(errors).keys())
            if errors_list[0] == 'password2':
                errors = str(json.loads(errors).get('password2')[0])
                
            elif errors_list[0] == 'username':
                errors = "This username is already taken"
            
    context = {
        "form":form,
        "errors":errors
    }
    return render(request,"site_users/register.html",context)