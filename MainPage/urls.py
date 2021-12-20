from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name="home"),
path("facemask/", views.facemask, name="facemask"),
path("machineshop/", views.machineshop, name="machineshop"),
# path("view/", views.view, name="index"),
# path("home/", views.home, name="home"),
path("facemask/create/", views.completed, name="close"),
# path("<int:id>", views.index, name="index"),
]
