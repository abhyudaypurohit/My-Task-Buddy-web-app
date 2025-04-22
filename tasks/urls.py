from django.urls import path
from .views import task_list, add_task, toggle_task_status, delete_task #import the view

urlpatterns = [
    path('', task_list, name='task_list'), #url for the homepage
    path('add/', add_task, name='add_task'), #url for adding tasks
    path('toggle/<int:task_id>/', toggle_task_status, name='toggle_task_status'),
    path('delete/<int:task_id>/', delete_task, name='delete_task')
]