from django.urls import path

from . import views


app_name = 'author'

urlpatterns = [
    path('', views.author_page, name='author_page'),
    path('delete/', views.delete, name="delete_profile")

]