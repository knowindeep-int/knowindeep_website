from django.urls import path

from . import views

app_name = 'blogs' 

urlpatterns = [
    path('like/<slug:blog>/<slug:slug>/',views.like_blog,name='like_blog'),
    path('',views.topics, name='index'),
    path('<slug:slug>/',views.subtopics, name='sub_topic'),
    path('<slug:slug>/<slug:blog>/',views.blog_post,name='blog_post'),
]