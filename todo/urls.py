from . import views
from django.contrib.auth.views import LoginView
from django.urls import path


urlpatterns = [
    path("", LoginView.as_view(template_name="custom-login.html"),
         name="login"),
    path("tasks/", views.TaskList.as_view(),
         name="home"),
    path("add-task/", views.AddTask.as_view(), name="add_task"),
    path("update-task/<int:pk>/", views.UpdateTask.as_view(),
         name="update_task"),
    path("delete-task/<int:pk>/", views.DeleteTask.as_view(),
         name="delete_task"),
    path("toggle-task/<int:pk>/", views.ToggleTask.as_view(),
         name="toggle_task"),
    path("search-task/", views.SearchTask.as_view(),
         name="search_task"),
]
