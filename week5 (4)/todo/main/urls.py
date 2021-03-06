from django.urls import path, re_path
from .views import todo_list, completed_todo_list

urlpatterns = [
    path('', todo_list),
    path('1/completed', completed_todo_list)
]