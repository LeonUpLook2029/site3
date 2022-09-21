from .models import Task
from django.forms import ModelForm, TextInput, DateInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "user", "date"]
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            "task": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
            "user": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите автора'}),
            "date": DateInput(attrs={'class': 'form-control', 'placeholder': 'Введите дату'}),

        }