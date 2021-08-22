from django.http import JsonResponse
from models.models import Task


def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return JsonResponse([t.as_dict() for t in tasks], safe=False)


def task_show(request, task_id: int):
    task = Task.objects.get(pk=task_id)
    return JsonResponse(task.as_dict())


def task_list_archived(request):
    tasks = Task.objects.archived().order_by('-created_at')
    return JsonResponse([t.as_dict() for t in tasks], safe=False)


def task_list_deleted(request):
    tasks = Task.objects.deleted().order_by('-created_at')
    return JsonResponse([t.as_dict() for t in tasks], safe=False)
