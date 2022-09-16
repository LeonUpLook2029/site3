from django.shortcuts import render
from django.http import HttpResponse

def index(requst):
    return render(requst, 'main/index.html')

def about(requst):
    return render(requst, 'main/about.html')

def price(requst):
    return render(requst, 'main/price.html')