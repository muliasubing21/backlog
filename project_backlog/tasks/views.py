from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Projects
from .models import Tasks
from .forms import TaskForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def index_tasks(request, project_id):
    tasks = Tasks.objects.filter(project_id=project_id)
    project = get_object_or_404(Projects, id=project_id)

    # Filter berdasarkan status
    status_filter = request.GET.get('status', '')
    if status_filter:
        tasks = tasks.filter(status=status_filter)

    # Filter berdasarkan assigned user
    assigned_filter = request.GET.get('assigned_to', '')
    if assigned_filter:
        tasks = tasks.filter(assigned_to__id=assigned_filter)

    # Mengirim daftar user untuk dropdown filter
    users = User.objects.all()

    context = {
        'project': project,
        'tasks': tasks,
        'users': users,
        'current_status': status_filter,
        'current_assigned': assigned_filter,
    }
    return render(request, 'tasks/index.html', context)

@login_required
def add_task(request, project_id):
    project = get_object_or_404(Projects,id=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('tasks:index_tasks', project_id=project.id)
    else:
        form = TaskForm()
    return render(request, 'tasks/form_task.html', {'form': form, 'project_id': project.id})

@login_required
def edit_task(request, task_id):
    tasks = get_object_or_404(Tasks, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('tasks:index_tasks', project_id=tasks.project_id)
    else:
        form = TaskForm(instance=tasks)
    return render(request, 'tasks/form_task.html', {'form': form, 'project_id': tasks.project_id})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    task.delete()
    return redirect('tasks:index_tasks', project_id=task.project_id)