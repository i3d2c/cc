from django.contrib import admin

from .models import Folder, Project, Category
from reversion.admin import VersionAdmin


@admin.register(Folder)
class FolderAdmin(VersionAdmin):
    list_display = ('name', 'id', 'owner', 'parent')
    #list_editable = ('name', 'id')
    list_filter = ('owner',)

@admin.register(Project)
class ProjectAdmin(VersionAdmin):
    list_display = ('name', 'id', 'owner', 'folder')
    #list_editable = ('name', 'id')
    list_filter = ('owner',)

@admin.register(Category)
class CategoryAdmin(VersionAdmin):
    pass
