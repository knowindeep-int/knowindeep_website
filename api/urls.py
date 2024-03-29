from django.urls import path

from .views import api_create_suggestion, api_detail_chapter_view, api_detail_chapter_update_view, api_all_detail_view, api_like_chapter_view, api_comment_project_view, fetchComments, increase_post_view, update_profile, search_project, api_save_draft, api_save_chapter_draft, api_get_languages_prereqs, api_create_project, api_get_project_absolute_url, api_get_chapter_absolute_url,api_create_chapter,api_update_status,api_create_suggestion, api_resolve_suggestion,api_get_suggestion,api_search_languages,api_delete_lang,api_create_bookmark,api_delete_bookmark,api_create_chapter_bookmark,api_delete_chapter_bookmark,api_get_ch_pr_au,api_get_blogs,api_update_user_status


app_name = "api"

urlpatterns = [
    path('update_profile/', update_profile, name='update_profile'),
    path('chapters/',api_all_detail_view),
    path('increaseView',increase_post_view,name='increase_view'),
    path('comments/',fetchComments,name='chapterComments'),
    path('search/', search_project, name='search'),
    path('getBlogs/', api_get_blogs, name = "get_blogs"),
    path('<slug:slug>/',api_detail_chapter_view),
    path('<slug:slug>/update',api_detail_chapter_update_view),
    path('chaptertopic/like',api_like_chapter_view,name='like-post'),
    path('chaptertopic/comment',api_comment_project_view,name="comment-post"),
    path('save_draft', api_save_draft, name="save_draft"),
    path('save_chapter_draft', api_save_chapter_draft, name="save_chapter_draft"),
    path('getLangPrereq', api_get_languages_prereqs, name = "get_lang_prereq"),
    path('createProject', api_create_project, name = "create_project"),
    path('getProjectAbsoluteURL', api_get_project_absolute_url, name = "get_project_absolute_url"),
    path('getChapterAbsoluteURL', api_get_chapter_absolute_url, name = "get_chapter_absolute_url"),
    path('createChapter', api_create_chapter, name = "create_chapter"),
    path('updateStatus', api_update_status, name = "update_status"),
    path('createSuggestion', api_create_suggestion, name = "create_suggestion"),
    path('resolveSuggestion', api_resolve_suggestion, name = "resolve_suggestion"),
    path('getSuggestion', api_get_suggestion, name = "get_suggestion"),
    path('searchLanguages', api_search_languages, name = "search_lang"),
    path('deleteLanguage', api_delete_lang, name = "delete_lang"),
    path('createBookmark', api_create_bookmark, name = "create_book"),
    path('deleteBookmark', api_delete_bookmark, name = "delete_book"),
    path('createChapterBookmark', api_create_chapter_bookmark, name = "create_chap_book"),
    path('deleteChapterBookmark', api_delete_chapter_bookmark, name = "delete_chap_book"),
    path('getChapProAuth', api_get_ch_pr_au, name = "get_ch_pr_au"),
    path('updateUserStatus', api_update_user_status, name = "update_status"),
]