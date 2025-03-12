from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('<uuid:project_id>', views.index_tasks, name='index_tasks'),
    path('add/<uuid:project_id>', views.add_task, name='add_task'),
    path('edit/<uuid:task_id>', views.edit_task, name='edit_task'),
    path('delete/<uuid:task_id>', views.delete_task, name='delete_task'),
]