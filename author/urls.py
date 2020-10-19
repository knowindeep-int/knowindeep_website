from django.urls import path

from . import views

from django.conf.urls import handler404


app_name = 'author'

urlpatterns = [
    path('<slug:slug>/', views.author_page, name='author_page')
]