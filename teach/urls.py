from django.urls import path

from .views import add_course, list_of_projects,text_editor, delete

app_name = "teach"

urlpatterns=[
    path('add/', add_course, name="add_course"),
    path('add/<int:pk>/', add_course, name="add_course"),
    path('', list_of_projects, name="list_of_projects"),
    path('chapter/<int:pk>',text_editor,name="chapter"),
    path('chapter/<int:pk>/<int:chapter_pk>',text_editor,name="chapter"),
    path('delete/<int:pk>/', delete, name="delete_ongoing_project")
]
