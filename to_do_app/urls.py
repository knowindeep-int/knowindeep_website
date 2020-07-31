from django.urls import path
from . import views


app_name = 'to_do_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('add_todo/',views.add_todo, name='add_todo'),
    path('delete_todo/<int:pk>',views.delete_todo, name='delete')
]