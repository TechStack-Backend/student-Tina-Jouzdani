from django.shortcuts import render, redirect
from .models import Developer, Project
from .forms import DeveloperForm, ProjectForm

def developers_list(request):
    developers = Developer.objects.prefetch_related('skills').all()
    return render(request, 'developers_list.html', {'developers': developers})

def projects_list(request):
    projects = Project.objects.prefetch_related('developers').all()
    return render(request, 'projects_list.html', {'projects': projects})

def developer_create(request):
    if request.method == 'POST':
        form = DeveloperForm(request.POST)
        if form.is_valid():
            dev = form.save()
            return redirect('developers_list')
    else:
        form = DeveloperForm()
    return render(request, 'developer_form.html', {'form': form})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            form.save_m2m()
            return redirect('projects_list')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form})
