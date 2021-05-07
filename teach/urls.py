from django.urls import path, register_converter

from .views import add_course, list_of_projects,text_editor, delete

from knowindeep.converters import NegativeIntConverter

app_name = "teach"

register_converter(NegativeIntConverter, 'negint')

urlpatterns=[
    path('add/', add_course, name="add_course"),
    path('add/<negint:pk>/', add_course, name="add_course"),
    path('', list_of_projects, name="list_of_projects"),
    path('chapter/<negint:pk>',text_editor,name="chapter"),
    path('chapter/<negint:pk>/<int:chapter_pk>',text_editor,name="chapter"),
    path('delete/<negint:pk>/', delete, name="delete_ongoing_project")
]
