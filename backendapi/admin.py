from django.contrib import admin

from .models import Folder, Project, Category

admin.site.register(Folder)
admin.site.register(Project)
admin.site.register(Category)
