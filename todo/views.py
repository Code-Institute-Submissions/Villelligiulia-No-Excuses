from django.shortcuts import render
from django.views import generic
from .models import Task
from django.urls import reverse_lazy
from .forms import TaskForm


class TaskList(generic.ListView):

    model = Task
    template_name = 'task.html'
    context_object_name = 'tasks'


class TaskAbout(generic.DetailView):

    model = Task
    template_name = 'about.html'
    context_object_name = 'about'


class AddTask(generic.CreateView):

    model = Task
    template_name = 'add_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('home')


class UpdateTask(generic.UpdateView):

    model = Task
    template_name = 'add_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('home')


class DeleteTask(generic.DeleteView):

    model = Task
    template_name = 'delete_task.html'
    context_object_name = 'task_to_delete'
    success_url = reverse_lazy('home')
