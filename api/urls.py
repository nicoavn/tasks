from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('tasks', views.task_list, name='task_list'),
    path('tasks/<uuid:task_id>', views.task_show, name='task_show'),
    path('tasks/archived', views.task_list_archived, name='task_list_archived'),
    path('tasks/deleted', views.task_list_deleted, name='task_list_deleted'),
]
