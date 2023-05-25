from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.TaskList.as_view(), name='home'),
    path('about/<int:pk>/', views.TaskAbout.as_view(), name='task'),
    path('add-task/', views.AddTask.as_view(), name='add_task'),
    path('update-task/<int:pk>/', views.UpdateTask.as_view(), name='update_task'),
    path('delete-task/<int:pk>/', views.DeleteTask.as_view(), name='delete_task'),
    path('toggle-task/<int:pk>/', views.ToggleTask.as_view(), name='toggle_task'),
    
]
