from django.urls import path

from . import views

urlpatterns = [
    path('projects/', views.projects, name='backendapi-projects'),
    path('projects/<int:id>/', views.project, name='backendapi-project'),
]
