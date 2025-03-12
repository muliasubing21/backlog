from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Projects

class ProjectForm(ModelForm):
    created_by = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=False,
        label='Select User :',
    )
    class Meta:
        model = Projects
        fields = ['name', 'description', 'created_by']
        labels = {
            'name': 'Name :',
            'description': 'Description :',
            'created_by': 'Select User :',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control' , 'style':'height: 100px'}),
            'description': forms.Textarea(attrs={'class': 'form-control' , 'style':'height: 100px'}),
        }