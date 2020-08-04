from django.urls import path

from .views import api_detail_blog_view, api_detail_blog_update_view, api_all_detail_view

urlpatterns = [
    path('blogs/',api_all_detail_view),
    path('<slug:slug>/',api_detail_blog_view),
    path('<slug:slug>/update',api_detail_blog_update_view)
]