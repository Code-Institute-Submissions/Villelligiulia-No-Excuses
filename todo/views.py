from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import redirect, get_object_or_404, render
from .models import Task
from django.urls import reverse_lazy
from .forms import TaskForm
from django.contrib import messages


class TaskList(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "task.html"
    context_object_name = "tasks"
    login_url = "login"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class ViewTask(generic.DetailView):
    model = Task
    template_name = 'view-task.html'
    context_object_name = "view_task"


class SearchTask(generic.ListView):
    model = Task
    template_name = "task.html"
    context_object_name = "tasks"

    def get_queryset(self):
        query = self.request.GET.get('task')
        user = self.request.user
        tasks = Task.objects.filter(
            user=user).order_by('title')
        if not query:
            messages.warning(self.request, 'Please enter a task to search.')
            return tasks
        searched_task = Task.objects.filter(
            user=user, title__icontains=query).order_by('title')
        if not searched_task:
            messages.warning(self.request, f"No results found for {query}")
            return tasks
        else:
            return searched_task


class AddTask(LoginRequiredMixin, generic.CreateView):
    model = Task
    template_name = "add_task.html"
    form_class = TaskForm
    success_url = reverse_lazy("home")
    login_url = "login"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "You added a new task")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("home")


class UpdateTask(LoginRequiredMixin, generic.UpdateView):
    model = Task
    template_name = "add_task.html"
    form_class = TaskForm
    success_url = reverse_lazy("home")
    login_url = "login"

    def form_valid(self, form):
        messages.success(self.request, "You have updated a task")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("home")


class DeleteTask(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "delete_task.html"
    context_object_name = "task_to_delete"

    success_url = reverse_lazy("home")
    login_url = "login"

    def delete(self, request, *args, **kwargs):
        messages.success(request, "You have deleted a task")
        return super().delete(request, *args, **kwargs)


class ToggleTask(LoginRequiredMixin, generic.View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.done = not task.done
        task.save()
        return redirect("home")

    login_url = "login"
