from django import forms
from .models import Curso

class CursoFormulario(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            "categoria",
            "titulo",
            "descripcion",
            "fecha_inicio",
            "carga_horaria",
            "activo",
        ]

        # (Opcional) mejora visual rápida: widgets
        widgets = {
            "fecha_inicio": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            "descripcion": forms.Textarea(attrs={"rows": 4}),
        }