from django import forms
from .models import Task
from django_summernote.widgets import SummernoteWidget


class TaskForm(forms.ModelForm):
    description = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Task
        fields = '__all__'
