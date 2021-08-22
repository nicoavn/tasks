from django.test import TestCase
from django.urls import reverse
import json
from django.utils import timezone

from models.models import Task


class TestTasksAPI(TestCase):
    def test_tasks_list(self):
        Task.objects.create(description="task1")
        Task.objects.create(description="task2")
        Task.objects.create(description="task3", deleted_at=timezone.now())
        Task.objects.create(description="task4", archived_at=timezone.now())
        response = self.client.get(reverse('api:task_list'))
        self.assertEqual(response.status_code, 200)
        parsed_response = json.loads(response.content)
        self.assertEqual(2, len(parsed_response))
        self.assertEqual('task1', parsed_response[0]['description'])
        self.assertEqual('task2', parsed_response[1]['description'])

    def test_tasks_list_archived(self):
        Task.objects.create(description="task1", archived_at=timezone.now())
        Task.objects.create(description="task2", archived_at=timezone.now())

        response = self.client.get(reverse('api:task_list_archived'))
        self.assertEqual(response.status_code, 200)
        parsed_response = json.loads(response.content)
        self.assertEqual(2, len(parsed_response))

    def test_tasks_list_deleted(self):
        Task.objects.create(description="task1", deleted_at=timezone.now())
        Task.objects.create(description="task2", deleted_at=timezone.now())

        response = self.client.get(reverse('api:task_list_deleted'))
        self.assertEqual(response.status_code, 200)
        parsed_response = json.loads(response.content)
        self.assertEqual(2, len(parsed_response))

    def test_task_show(self):
        task = Task.objects.create(description="task1")
        response = self.client.get(reverse('api:task_show', kwargs={'task_id': task.pk}))
        self.assertEqual(response.status_code, 200)
        parsed_response = json.loads(response.content)
        self.assertEqual(str(task.pk), parsed_response['task_id'])
