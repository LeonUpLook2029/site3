from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
# не требуется т.к. все обьекты в словарь
# from .models import User
# from .models import Date
from .forms import TaskForm

def index(requst):
    task = Task.objects.all()
    # user = User.objects.all() не требуется т.к. все обьекты в словарь
    # date = Date.objects.all()
    return render(requst, 'main/index.html', {'title': 'Главная страница', 'tasks': task})
# {, 'users': user, 'dates': date} не требуется т.к. все обьекты в словарь 'tasks'
def about(requst):
    return render(requst, 'main/about.html')

def create(requst):
    error = ""
    if requst.method == 'POST':
        form = TaskForm(requst.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = 'Ввод данных был не верный'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(requst, 'main/create.html', context)

def out(requst):
    return render(requst, 'main/out.html')

def price(requst):
    return render(requst, 'main/price.html')