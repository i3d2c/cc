from django.urls import path

from . import views

urlpatterns = [
    path('projects/', views.projects, name='front-projects'),
    path('projects/<int:id>/', views.project, name='front-project'),
]
