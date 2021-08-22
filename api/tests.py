from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class TestTasksAPI(TestCase):
    def test_tasks_list(self):
        response = self.client.get(reverse('api:task_list'))
        self.assertEqual(response.status_code, 200)
        # self.assertQuerysetEqual(response.context['data'], {})
