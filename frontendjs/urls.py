from django.urls import path

from . import views

urlpatterns = [
    path('projects/', views.projects, name='front-projects'),
    # If you change following url, change it also in frontendjs/projects.html
    # event dblclick.jstree
    path('projects/<int:id>/', views.project, name='front-project'),
]
