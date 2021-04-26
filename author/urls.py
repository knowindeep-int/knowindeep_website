from django.urls import path

from . import views


app_name = 'author'

urlpatterns = [
    
    path('/delete/<int:pk>', views.delete, name="delete_author"),    
    path('/', views.author_page, name='author_page'),
]