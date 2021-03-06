from django.shortcuts import render
import datetime


# Create your views here.
def todo_list(request):
    todos = [
        {
            'task': 'Task 1',
            'created': datetime.date(2021, 1, 1).strftime("%Y/%m/%d"),
            'due': datetime.date(2021, 2, 1).strftime("%Y/%m/%d"),
            'owner': 'admin',
            'mark': 'Not Done'},
        {
            'task': 'Build a house',
            'created': datetime.date(2020, 2, 6).strftime("%Y/%m/%d"),
            'due': datetime.date(2021, 4, 1).strftime("%Y/%m/%d"),
            'owner': 'dad',
            'mark': 'Not Done'
        },
        {
            'task': 'Build a pool',
            'created': datetime.date(2020, 2, 6).strftime("%Y/%m/%d"),
            'due': datetime.date(2021, 4, 1).strftime("%Y/%m/%d"),
            'owner': 'dad',
            'mark': 'Not Done'
        },
        {
            'task': 'Buy groceries',
            'created': datetime.date(2021, 2, 26).strftime("%Y/%m/%d"),
            'due': datetime.date(2021, 2, 27).strftime("%Y/%m/%d"),
            'owner': 'mom',
            'mark': 'Not Done'
        },
    ]
    context = {
        'todos': todos,
    }
    return render(request, 'todo_list.html', context=context)

def completed_todo_list(request):
    todos = [
        {
            'task': 'Task 1',
            'created': datetime.date(2021, 1, 1).strftime("%Y/%m/%d"),
            'due': datetime.date(2021, 2, 1).strftime("%Y/%m/%d"),
            'owner': 'admin',
            'mark': 'Done'},
        {
            'task': 'Build a house',
            'created': datetime.date(2020, 2, 6).strftime("%Y/%m/%d"),
            'due': datetime.date(2021, 4, 1).strftime("%Y/%m/%d"),
            'owner': 'dad',
            'mark': 'Done'
        },
        {
            'task': 'Build a pool',
            'created': datetime.date(2020, 2, 6).strftime("%Y/%m/%d"),
            'due': datetime.date(2021, 4, 1).strftime("%Y/%m/%d"),
            'owner': 'dad',
            'mark': 'Done'
        },
        {
            'task': 'Buy groceries',
            'created': datetime.date(2021, 2, 26).strftime("%Y/%m/%d"),
            'due': datetime.date(2021, 2, 27).strftime("%Y/%m/%d"),
            'owner': 'mom',
            'mark': 'Done'
        },
    ]
    context = {
        'todos': todos,
    }
    return render(request, 'completed_todo_list.html', context=context)
