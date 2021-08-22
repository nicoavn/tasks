import uuid
from django.db import models

# Create your models here.

class Task(models.Model):
	task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	description = models.CharField(max_length=254, null=True)
	task_type = models.CharField(max_length=40)
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now=True)
	archived_at = models.DateTimeField(null=True)
