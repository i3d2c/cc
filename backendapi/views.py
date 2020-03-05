from django.shortcuts import render, get_object_or_404
from backendapi.models import Project, Folder
from django.contrib.auth.decorators import login_required

@login_required
def projects(request):
    projects = Project.objects.filter(owner=request.user)
    folders = Folder.objects.all()
    return render(request, 'backendapi/projects.html', {'projects': projects, 'folders': folders})

@login_required
def project(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, 'backendapi/project.html', {'project': project})
