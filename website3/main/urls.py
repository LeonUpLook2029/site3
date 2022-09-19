from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('create', views.create, name="create"),
    path('out', views.out, name="out"),
    path('price', views.price, name="price"),
]