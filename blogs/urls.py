from django.urls import path

from . import views


app_name = 'blogs'

urlpatterns = [
    path('<slug:slug>/',views.blogs, name='sub_topic'),
    path('<slug:slug>/<slug:topic>/<slug:subtopic>/',views.subtopics,name='sub_topic_page')
]