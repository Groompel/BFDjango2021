from django.shortcuts import render
import datetime
from .models import TodoList, Task


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
