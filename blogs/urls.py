from django.urls import path

from . import views


app_name = 'blogs'

urlpatterns = [
    path('<slug:slug>/',views.blogs, name='sub_topic'),
]