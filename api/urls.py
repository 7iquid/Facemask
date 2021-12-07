from django.urls import path
from django.contrib import admin
from django.conf.urls import include
from .views import MachineStatus , Home, StatsMachine


urlpatterns = [
    path('', MachineStatus.as_view()),
    path('<str:machine_no>/', StatsMachine, name="StatsMachine"),
    path('test', Home, name="home"),

]
