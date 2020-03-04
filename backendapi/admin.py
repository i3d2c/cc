from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Folder, Project, Category

admin.site.register(Folder, DraggableMPTTAdmin)
admin.site.register(Project)
admin.site.register(Category)
