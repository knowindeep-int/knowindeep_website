from django.urls import path

from . import views


app_name = 'blogs' 

urlpatterns = [
    path('',views.topics, name='index'),
    path('remove/<slug:slug>/', views.remove, name='remove'),
    path('approve/<slug:slug>/', views.approve, name = 'approve'),
    path('<slug:slug>/',views.subtopics, name='sub_topic'),
    path('<slug:slug>/<slug:chapter>/',views.chapter_post,name='chapter_post'),
]