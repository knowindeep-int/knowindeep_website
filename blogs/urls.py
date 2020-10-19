from django.urls import path

from . import views

from django.conf.urls import handler404


app_name = 'blogs' 

urlpatterns = [
    path('',views.topics, name='index'),
    path('remove/<slug:slug>/', views.remove, name='remove'),
    path('approve/<slug:slug>/', views.approve, name = 'approve'),
    path('<slug:slug>/',views.subtopics, name='sub_topic'),
    path('<slug:slug>/<slug:blog>/',views.blog_post,name='blog_post'),
]