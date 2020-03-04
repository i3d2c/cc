from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from mptt.models import MPTTModel, TreeForeignKey

class Folder(MPTTModel):
    name = models.CharField(max_length=64, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    content = JSONField(default=dict, blank=True)
    infos = JSONField(default=dict, blank=True)
    actions = JSONField(default=list, blank=True)
    archived = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return "{} ({})".format(self.name, self.owner.username)


class Category(models.Model):
    name = models.CharField(max_length=256)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = JSONField(default=dict, blank=True)
    archived = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
