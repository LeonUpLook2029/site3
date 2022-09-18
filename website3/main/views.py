from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
# не требуется т.к. все обьекты в словарь
# from .models import User
# from .models import Date

def index(requst):
    task = Task.objects.all()
    # user = User.objects.all() не требуется т.к. все обьекты в словарь
    # date = Date.objects.all()
    return render(requst, 'main/index.html', {'title': 'Главная страница', 'tasks': task})
# {, 'users': user, 'dates': date} не требуется т.к. все обьекты в словарь 'tasks'
def about(requst):
    return render(requst, 'main/about.html')

def price(requst):
    return render(requst, 'main/price.html')