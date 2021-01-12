from django.urls import path

from .views import api_detail_chapter_view, api_detail_chapter_update_view, api_all_detail_view, api_like_chapter_view, api_comment_chapter_view, fetchComments, increase_post_view, update_profile, search_project, api_save_draft, api_save_chapter_draft, api_get_languages_prereqs, api_create_project, api_get_project_absolute_url, api_get_chapter_absolute_url,api_create_chapter,api_update_status


app_name = "api"

urlpatterns = [
    path('update_profile/', update_profile, name='update_profile'),
    path('chapters/',api_all_detail_view),
    path('increaseView',increase_post_view,name='increase_view'),
    path('comments/',fetchComments,name='chapterComments'),
    path('search/', search_project, name='search'),
    path('<slug:slug>/',api_detail_chapter_view),
    path('<slug:slug>/update',api_detail_chapter_update_view),
    path('chaptertopic/like',api_like_chapter_view,name='like-post'),
    path('chaptertopic/comment',api_comment_chapter_view,name="comment-post"),
    path('save_draft', api_save_draft, name="save_draft"),
    path('save_chapter_draft', api_save_chapter_draft, name="save_chapter_draft"),
    path('getLangPrereq', api_get_languages_prereqs, name = "get_lang_prereq"),
    path('createProject', api_create_project, name = "create_project"),
    path('getProjectAbsoluteURL', api_get_project_absolute_url, name = "get_project_absolute_url"),
    path('getChapterAbsoluteURL', api_get_chapter_absolute_url, name = "get_chapter_absolute_url"),
    path('createChapter', api_create_chapter, name = "create_chapter"),
    path('updateStatus', api_update_status, name = "update_status")

]