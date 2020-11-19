from django.urls import path

from .views import add_course

app_name = "teach"

urlpatterns=[
    path('', add_course, name="add_course")
]
