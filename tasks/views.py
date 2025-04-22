from django.shortcuts import render, redirect, get_object_or_404
from .models import Task  # Importing Task model
from .forms import TaskForm
from datetime import datetime

# Function to list all tasks
def task_list(request):
    filter_type = request.GET.get('filter')

    if filter_type == 'pending':
        tasks = Task.objects.filter(completed=False).order_by('due_date')

    elif filter_type == 'completed':
        tasks = Task.objects.filter(completed=True).order_by('due_date')

    else:
        tasks = Task.objects.all().order_by('due_date')  # Fetch all tasks, sorted by due date
    
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'filter_type': filter_type})  # Pass tasks to template

# Function to add a new task
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'tasks/add_task.html', {'form': form})

# Function to toggle the completion status of a task
def toggle_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed  # Toggle completion status
    task.save()
    return redirect('task_list')

# Function to delete a task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
