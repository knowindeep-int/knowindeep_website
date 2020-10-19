from django.urls import path

from .views import api_detail_blog_view, api_detail_blog_update_view, api_all_detail_view, api_like_blog_view, api_comment_blog_view, fetchComments, increase_post_view


app_name = "api"

urlpatterns = [
    path('blogs/',api_all_detail_view),
    path('increaseView',increase_post_view,name='increase_view'),
    path('comments/',fetchComments,name='blogComments'),
    path('<slug:slug>/',api_detail_blog_view),
    path('<slug:slug>/update',api_detail_blog_update_view),
    path('blogtopic/like',api_like_blog_view,name='like-post'),
    path('blogtopic/comment',api_comment_blog_view,name="comment-post"),
]