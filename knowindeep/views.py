from django.shortcuts import render, redirect


def about_us(request):
    return render(request, "new/about/about_us.html")

def privacy_policy(request):
    return render(request, "new/policy/privacy_policy.html")

def terms_of_use(request):
    return render(request, "new/policy/terms_of_use.html")

def terms_for_creators(request):
    return render(request, "new/policy/terms_for_creators.html")