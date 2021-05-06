from django.urls import path

from . import views


app_name = 'author'

urlpatterns = [

    path('profile/delete/', views.delete, name="delete_profile"),
    path('author/<str:slug>/', views.author_page, name='author_page'),
]