from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False  # Optional due date
    )

    class Meta:
        model = Task
        fields = ['title', 'due_date']
