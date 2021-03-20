from django.shortcuts import render
import datetime
from .models import TodoList, Task
from rest_framework import generics

# Create your views here.


def todo_list(request):
    lists = TodoList.objects.all()

    res = []
    for todo_list in lists:
        tasks = Task.objects.filter(task_list=todo_list)
        res.append([todo_list, tasks])

    context = {
        'lists': res,
    }
    return render(request, 'todo_list.html', context=context)


def completed_todo_list(request, id):
    todo_list = TodoList.objects.get(id=id)

    tasks = Task.objects.filter(task_list=todo_list, completed=True)

    context = {
        'todo_list': todo_list,
        'tasks': tasks
    }
    return render(request, 'completed_todo_list.html', context=context)

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAdminUser]

#     def list(self, request):
    # Note the use of `get_queryset()` instead of `self.queryset`
    # queryset = self.get_queryset()
    # serializer = UserSerializer(queryset, many=True)
    # return Response(serializer.data)
