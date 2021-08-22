from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from models.models import Task
# Create your views here.

def task_list(request):
    tasks = Task.objects.filter().order_by('-created_at')
    task_list = serializers.serialize('json', tasks)
    return HttpResponse(task_list, content_type="text/json-comment-filtered")
