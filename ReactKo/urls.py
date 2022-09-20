from django.urls import path, include, re_path
from . import views
# from django.views.generic import TemplateView
urlpatterns = [
path("", views.home, name="home"),

# path("<int:id>", views.index, name="index"),
]
# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]