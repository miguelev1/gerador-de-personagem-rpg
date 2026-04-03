# geradordepersonagem/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("",      views.index,      name="index"),
    path("gerar/", views.gerar_ajax, name="gerar_ajax"),
]
