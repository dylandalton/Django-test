from django.urls import path

from pyExam import views

urlpatterns = [
    path('', views.index, name='index'),
]