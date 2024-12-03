import json
from django.shortcuts import render, redirect
from django.contrib import messages

# Helper function to read tasks from the JSON file
def read_tasks():
    try:
        with open('todo/data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if the file does not exist

# Helper function to write tasks to the JSON file
def write_tasks(tasks):
    with open('todo/data.json', 'w') as file:
        json.dump(tasks, file)

# View to display the To-Do list
def index(request):
    tasks = read_tasks()
    return render(request, 'index.html', {'tasks': tasks})

# View to add a new task
def add_task(request):
    if request.method == 'POST':
        new_task = request.POST.get('task')
        tasks = read_tasks()
        tasks.append({'title': new_task, 'completed': False})
        write_tasks(tasks)
        messages.success(request, 'Task created successfully!')
        return redirect('index')
    return redirect('index')

# View to update a task's completion status
def update_task(request, task_title):
    tasks = read_tasks()
    for task in tasks:
        if task['title'] == task_title:
            task['completed'] = not task['completed']
    write_tasks(tasks)
    messages.success(request, 'Task updated successfully!')
    return redirect('index')

# View to delete a task
def delete_task(request, task_title):
    tasks = read_tasks()
    tasks = [task for task in tasks if task['title'] != task_title]
    write_tasks(tasks)
    messages.success(request, 'Task deleted successfully!')
    return redirect('index')

# View to edit a task's title
def edit_task(request, task_title):
    tasks = read_tasks()
    if request.method == 'POST':
        new_title = request.POST.get('new_task_title')
        for task in tasks:
            if task['title'] == task_title:
                task['title'] = new_title
                break
        write_tasks(tasks)
        messages.success(request, 'Task edited successfully!')
        return redirect('index')
    return render(request, 'edit_task.html', {'task_title': task_title})