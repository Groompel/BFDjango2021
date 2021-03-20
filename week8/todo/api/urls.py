from django import urls
from api.views import TaskView, TodoListView, get_list_completed_tasks
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('todos', TodoListView)
router.register('tasks', TaskView)

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/<int:list_id>/completed', get_list_completed_tasks)
]
