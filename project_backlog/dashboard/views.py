from django.shortcuts import render
from projects.models import Projects
from tasks.models import Tasks
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    projects_count = Projects.objects.count()
    tasks_count = Tasks.objects.count()
    tasks_todo = Tasks.objects.filter(status='TODO').count()
    tasks_in_progress = Tasks.objects.filter(status='IN_PROGRESS').count()
    tasks_completed = Tasks.objects.filter(status='DONE').count()
    tasks_pending = tasks_count - tasks_completed
    recent_tasks = Tasks.objects.order_by('-created_at')[:5]

    context = {
        'projects_count': projects_count,
        'tasks_count': tasks_count,
        'tasks_todo': tasks_todo,
        'tasks_in_progress': tasks_in_progress,
        'tasks_completed': tasks_completed,
        'tasks_pending': tasks_pending,
        'recent_tasks': recent_tasks,
    }
    return render(request, 'dashboard/index.html', context)