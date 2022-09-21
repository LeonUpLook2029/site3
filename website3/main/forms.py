from .models import Task
from django.forms import ModelForm, TextInput, DateInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "user", "date"]
        widgets = {"title": TextInput(attrs={'class':'from-control', 'placeholder':'Введите название'}),
            "task": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Введите описание'
            }),
            "user": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Введите автора'
            }),
            "date": DateInput(attrs={
                'class': 'from-control',
                'placeholder': 'Введите дату'
            }),

        }