from django.contrib import admin
from .models import Task, TodoList

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ['task', 'created', 'due', 'completed']
    list_editable = ['completed']


class TodoListAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Task, TaskAdmin)
admin.site.register(TodoList, TodoListAdmin)
