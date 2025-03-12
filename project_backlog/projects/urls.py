from django.urls import path, include

from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.index, name='index_projects'),
    path('add/', views.add_project, name='add_project'),
    path('edit/<uuid:project_id>', views.edit_project, name='edit_project'),
    path('delete/<uuid:project_id>', views.delete_project, name='delete_project'),
]