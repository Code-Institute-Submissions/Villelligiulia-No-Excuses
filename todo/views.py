from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import redirect, get_object_or_404
from .models import Task
from django.urls import reverse_lazy
from .forms import TaskForm


class TaskList(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'task.html'
    context_object_name = 'tasks'
    login_url = 'login'


class TaskAbout(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = 'about.html'
    context_object_name = 'about'
    login_url = 'login'


class AddTask(LoginRequiredMixin, generic.CreateView):
    model = Task
    template_name = 'add_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('home')
    login_url = 'login'


class UpdateTask(LoginRequiredMixin, generic.UpdateView):
    model = Task
    template_name = 'add_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('home')
    login_url = 'login'


class DeleteTask(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = 'delete_task.html'
    context_object_name = 'task_to_delete'
    success_url = reverse_lazy('home')
    login_url = 'login'


class ToggleTask(LoginRequiredMixin, generic.View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.done = not task.done
        task.save()
        return redirect('home')
    login_url = 'login'
