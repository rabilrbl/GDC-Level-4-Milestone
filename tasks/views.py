from django.shortcuts import render, redirect
# Add all your views here

def index(request):
    return redirect('/tasks/')

# TASKS List
TASK = []
COMPLETED_TASKS = []

# Add task to TASKS List
def add_task(request):
    task = request.GET.get('task')
    TASK.append(task)
    return redirect('/tasks/')

# Delete task from TASKS List
def delete_task(request, task_id):
    TASK.pop(task_id-1)
    return redirect('/tasks/')

# Complete task from TASKS List
def complete_task(request, task_id):
    task = TASK.pop(task_id-1)
    COMPLETED_TASKS.append(task)
    return redirect('/tasks/')

# Show TASKS List
def tasks(request):
    return render(request, 'tasks.html', {'tasks': TASK})

# Delete task from COMPLETED_TASKS List
def delete_completed_task(request, task_id):
    COMPLETED_TASKS.pop(task_id-1)
    return redirect('/tasks/')

# Show COMPLETED_TASKS List
def completed_tasks(request):
    return render(request, 'completed_tasks.html', {'completed_tasks': COMPLETED_TASKS})

# Show both TASKS and COMPLETED_TASKS List
def all_tasks(request):
    return render(request, 'all_tasks.html', {'tasks': TASK, 'completed_tasks': COMPLETED_TASKS})
