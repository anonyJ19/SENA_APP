from django.db import models

class Aprendiz(models.Model):
    documento = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    telefono = models.CharField(max_length=10, null=True)
    fecha_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=100, null=True)
    programa = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"

    def nombre_completo(self):
        return f"{self.nombre} - {self.apellido}"
