from django.urls import path

from .views import api_detail_blog_view, api_detail_blog_update_view

urlpatterns = [
    path('<slug:slug>/',api_detail_blog_view),
    path('<slug:slug>/update',api_detail_blog_update_view)
]