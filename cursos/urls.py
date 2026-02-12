from django.urls import path
from . import views

app_name = "cursos" # Revisar con y sin app_name

urlpatterns = [
    path("", views.lista_cursos, name="lista"), # Read
    path("nuevo/", views.crear_curso, name="crear"),
    path("<int:id_curso>",views.detalle_curso, name="detalle"),
    path("<int:id_curso>/editar/", views.editar_curso, name="editar"),
    path("<int:id_curso>/eliminar/", views.eliminar_curso, name="eliminar"),

]