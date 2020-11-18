from django.urls import path

from . import views

app_name = "teach"

urlpatterns=[
    path('', views.sample, name="index")
]
print('Hello')