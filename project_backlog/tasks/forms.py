from django import forms
from django.forms import ModelForm
from .models import Tasks

class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'description', 'assigned_to', 'status']
        labels = {
            'name': 'Task Name',
            'description': 'Description',
            'assigned_to': 'Assigned To',
            'status': 'Status',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style':'height: 100px'}),
            'assigned_to': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }