from django.urls import path

from .views import add_course, list_of_projects,text_editor

app_name = "teach"

urlpatterns=[
    path('add/', add_course, name="add_course"),
    path('add/<int:pk>/', add_course, name="add_course"),
    path('', list_of_projects, name="list_of_projects"),
    path('chapter',text_editor,name="chapter")
]
