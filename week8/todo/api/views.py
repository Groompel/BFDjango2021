from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from main.models import Task, TaskModelSerializerList, TaskModelSerializerRetrieve, TodoList, TodoListSerializerList, TodoListSerializerRetrieve
# Create your views here.


class TodoListView(ModelViewSet):
    queryset = TodoList.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TodoListSerializerRetrieve
        else:
            return TodoListSerializerList


class TaskView(ModelViewSet):
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TaskModelSerializerRetrieve
        else:
            return TaskModelSerializerList


def get_list_completed_tasks(request, list_id):
    tasks = Task.objects.filter(id=list_id, completed=True)
    return JsonResponse(TaskModelSerializerList(tasks, many=True).data, safe=False)
