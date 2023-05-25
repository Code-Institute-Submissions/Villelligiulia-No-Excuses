from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='home'),
    path('about/<int:pk>/', views.TaskAbout.as_view(), name='task'),
    path('add-task/', views.AddTask.as_view(), name='add_task')
]
