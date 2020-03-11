from django.contrib import admin

from .models import Folder, Project, Category

class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'active', 'archived')
    list_editable = ('active', 'archived')
    list_filter = ('active', 'archived')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'active', 'archived')
    list_editable = ('active', 'archived')
    list_filter = ('active', 'archived')

admin.site.register(Folder, FolderAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)

