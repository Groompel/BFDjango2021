from .models import Task, TodoList
from django.contrib import admin

# Register your models here.
admin.site.register(TodoList)
admin.site.register(Task)
