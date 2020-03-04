from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

class Project(models.Model):
    name = models.CharField(max_length=1024)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
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
