from django.http import JsonResponse
from models.models import Task


def task_list(request):
    tasks = Task.objects.filter().order_by('-created_at')
    return JsonResponse([t.as_dict() for t in tasks], safe=False)
