import uuid
from django.db import models
from datetime import datetime


class TaskManager(models.Manager):
    def all(self):
        return self.filter(archived_at__isnull=True, deleted_at__isnull=True)

    def archived(self):
        return self.filter(archived_at__isnull=False)

    def deleted(self):
        return self.filter(deleted_at__isnull=False)


class Task(models.Model):
    objects = TaskManager()
    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=254, null=True)
    task_type = models.CharField(max_length=40)
    created_at = models.DateTimeField(blank=True, null=True, editable=False)
    updated_at = models.DateTimeField(blank=True, null=True, editable=False)
    deleted_at = models.DateTimeField(blank=True, null=True, editable=False)
    archived_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.task_id:
            self.created_at = datetime.now()
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.description

    def as_dict(self):
        return dict((f.name, getattr(self, f.name)) for f in self._meta.fields)
