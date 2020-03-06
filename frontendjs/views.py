from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from backendapi.models import Project, Folder

@login_required
def projects(request):
    return render(request, 'frontendjs/projects.html')

@login_required
def project(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, 'frontendjs/project.html', {'project': project})
