from django.shortcuts import render


from django.http import HttpResponse

def index(requst):
    return HttpResponse('<h2>Django blog!</h2>')