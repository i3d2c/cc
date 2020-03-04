from django.shortcuts import render
from backendapi.models import Project, Folder

def projects(request):
    if request.user.is_authenticated:
        projects = Project.objects.filter(owner=request.user)
        folders = Folder.objects.all()
        return render(request, 'backendapi/projects.html', {'projects': projects, 'folders': folders})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
