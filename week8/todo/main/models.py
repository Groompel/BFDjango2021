from django.db import models
# from django.contrib.auth.models import User
from custom_auth.models import Profile
from rest_framework.serializers import ModelSerializer

# Create your models here.


class TodoList(models.Model):
    name = models.CharField(
        max_length=255, verbose_name='Name', null=False, blank=False)

    class Meta:
        verbose_name = 'Task List'
        verbose_name_plural = 'Task Lists'

    def __str__(self):
        return self.name


class Task(models.Model):
    task = models.CharField(max_length=255, null=False,
                            blank=False, verbose_name='Task')
    created = models.DateField(
        auto_created=True, auto_now_add=True, verbose_name='Created', )
    due = models.DateField(verbose_name='Due on')
    owner = models.ForeignKey(
        Profile, null=False, blank=False, on_delete=models.CASCADE, default=1)
    completed = models.BooleanField(verbose_name='Completed', default=False)
    task_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.task


class TaskModelSerializerList(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'task', 'created', 'completed')


class TaskModelSerializerRetrieve(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'task', 'created', 'owner', 'completed', 'task_list')


class TodoListSerializerList(ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'name')


class TodoListSerializerRetrieve(ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'name')
