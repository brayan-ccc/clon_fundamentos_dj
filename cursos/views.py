from django.shortcuts import render
from .models import Curso
# Create your views here.

def lista_cursos(request):
    # cursos = (Curso.objects.select_related("categoria").order_by("-fecha_inicio","titulo"))
    cursos = (
        Curso.objects
        .select_related("categoria")
        .order_by("fecha_inicio","titulo")
    )

    contexto = {"cursos":cursos}

    return render(request, "cursos/lista_cursos.html", contexto)
