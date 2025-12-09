from django.contrib import admin

from .models import AprendizCurso, Curso, InstructorCurso

admin.site.register(Curso)
admin.site.register(InstructorCurso)
admin.site.register(AprendizCurso)
# Register your models here.
