from django.shortcuts import render
from django.http import HttpResponse

def index(requst):
    return HttpResponse('<h4>Hello!</h4>')

def about(requst):
    return HttpResponse('<h2>About us</h2>')