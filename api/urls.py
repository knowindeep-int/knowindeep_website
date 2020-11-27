from django.urls import path

from .views import api_detail_blog_view, api_detail_blog_update_view, api_all_detail_view, api_like_chapter_view, api_comment_chapter_view, fetchComments, increase_post_view, update_profile


app_name = "api"

urlpatterns = [
    path('update_profile/', update_profile, name='update_profile'),
    path('blogs/',api_all_detail_view),
    path('increaseView',increase_post_view,name='increase_view'),
    path('comments/',fetchComments,name='blogComments'),
    path('<slug:slug>/',api_detail_blog_view),
    path('<slug:slug>/update',api_detail_blog_update_view),
    path('chaptertopic/like',api_like_chapter_view,name='like-post'),
    path('chaptertopic/comment',api_comment_chapter_view,name="comment-post"),
]