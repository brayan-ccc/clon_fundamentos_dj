from django.db import models

# Create your models here.
# Para nombre de clase ya no usamos snake_case
# Para nombre de clase usaremos PascalCase
class Categoria(models.Model):
    # variable(atributo/columna) = models.TipoDato("Nombre de campo para humanos")
    nombre = models.CharField("nombre", max_length=50, unique=True)
    descripcion = models.TextField("descripción", blank=True)

    # Las siguientes son útiles para el Admin de DJANGO, no afectan la estructura de la tabla
    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    # Relación 1:N con la tabla Categoria
    # ci = models.CharField("carnet", max_length=10, primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="cursos", verbose_name = "categoría")
    
    # Campos
    titulo = models.CharField("título", max_length=100)
    descripcion = models.TextField("descripción", blank=True)
    fecha_inicio = models.DateField("fecha de inicio")
    carga_horaria = models.PositiveSmallIntegerField("carga horaria", default=0)
    activo = models.BooleanField("activo", default=True)

    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"

    def __str__(self):
        return self.titulo