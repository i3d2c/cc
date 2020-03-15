from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

class Folder(models.Model):
    name = models.CharField(max_length=64, unique=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, null=True, on_delete=models.CASCADE)
    content = JSONField(default=dict, blank=True)
    infos = JSONField(default=dict, blank=True)
    actions = JSONField(default=list, blank=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.owner.username)


class Category(models.Model):
    name = models.CharField(max_length=256)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = JSONField(default=dict, blank=True)
