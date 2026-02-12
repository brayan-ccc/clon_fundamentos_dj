from django.urls import path
from . import views

# app_name = "cursos" # Revisar con y sin app_name

urlpatterns = [
    path("", views.lista_cursos, name="lista"), # Read

]