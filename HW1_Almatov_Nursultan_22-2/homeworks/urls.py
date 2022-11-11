from django.urls import path
from . import views

app_name = 'homeworks'

urlpatterns = [
    path('', views.main, name='links'),
    path('hello/', views.hello, name='hello'),
    path('goodby/', views.goodby, name='goodby'),
    path('now_date/', views.now_date, name='date'),
]