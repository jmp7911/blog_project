from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('chat/', views.chat, name='chat'),
    path('view/', views.view, name='view'),
    path('write/', views.write, name='write'),
]
