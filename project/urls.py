from django.urls import path

from . import views


app_name = 'project' 

urlpatterns = [
    path('',views.topics, name='index'),
    path('remove/<slug:slug>/<slug:method>', views.remove, name='remove'),
    path('approve/<slug:slug>/<slug:method>', views.approve, name = 'approve'),
    path('<slug:slug>/',views.subtopics, name='sub_topic'),
    path('<slug:slug>/<slug:chapter>/',views.chapter_post,name='chapter_post'),
    # path('all_blogs',views.list_all_blogs,name='blogs_list'),
]