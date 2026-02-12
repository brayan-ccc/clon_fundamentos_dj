from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso
from .forms import CursoFormulario
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

def detalle_curso(request, id_curso):
    curso = get_object_or_404(Curso, pk = id_curso)
    
    return render(request, "cursos/detalle_curso.html",{"curso":curso})


def crear_curso(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("cursos:lista")  # PRG
    else:
        formulario = CursoFormulario()

    return render(request, "cursos/formulario_curso.html", {
        "formulario": formulario,
        "modo": "crear",
        "titulo_pagina": "Crear curso",
    })


def editar_curso(request, id_curso):
    curso = get_object_or_404(Curso, pk=id_curso)

    if request.method == "POST":
        formulario = CursoFormulario(request.POST, instance=curso)
        if formulario.is_valid():
            formulario.save()
            return redirect("cursos:detalle", id_curso=curso.pk)  # PRG
    else:
        formulario = CursoFormulario(instance=curso)

    return render(request, "cursos/formulario_curso.html", {
        "formulario": formulario,
        "modo": "editar",
        "titulo_pagina": "Editar curso",
        "curso": curso,
    })


def eliminar_curso(request, id_curso):
    curso = get_object_or_404(Curso, pk=id_curso)

    if request.method == "POST":
        curso.delete()
        return redirect("cursos:lista")  # PRG

    return render(request, "cursos/confirmar_eliminar.html", {"curso": curso})