from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Main page
    path('add/', views.add_task, name='add_task'),  # Add task
    path('update/<str:task_title>/', views.update_task, name='update_task'),  # Update task
    path('delete/<str:task_title>/', views.delete_task, name='delete_task'),  # Delete task
    path('edit/<str:task_title>/', views.edit_task, name='edit_task'), #edit task
]