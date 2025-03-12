from django.shortcuts import render, redirect, get_object_or_404
from .models import Projects
from .forms import ProjectForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    all_projects = Projects.objects.all()
    
    filter_all_projects = all_projects

    # Filter berdasarkan project
    project_filter = request.GET.get('filter_project', '')
    if project_filter:
        filter_all_projects = filter_all_projects.filter(id=project_filter)

    # Filter berdasarkan created_by
    created_filter = request.GET.get('filter_created_by', '')
    if created_filter:
        filter_all_projects = filter_all_projects.filter(created_by__id=created_filter)

    # Mengirim daftar user untuk dropdown filter
    users = User.objects.all()

    context = {
        'all_projects': all_projects,
        'projects': filter_all_projects,
        'users': users,
        'current_project': project_filter,
        'current_created': created_filter,
    }
    return render(request, 'projects/index.html', context)

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('projects:index_projects')
    else:
        form = ProjectForm()
    return render(request, 'projects/form_project.html', {'form': form})

@login_required
def edit_project(request, project_id):
    project = get_object_or_404(Projects, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects:index_projects')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/form_project.html', {'form': form})

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Projects, id=project_id)
    project.delete()
    return redirect('projects:index_projects')