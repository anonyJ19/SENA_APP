from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from unittest import loader
from SENA_APP.instructores.models import instructor


def instructores(request):
    lista_instructor = instructor.objects.all().values()
    template = loader.get_template('lista_instructores.html')
    context = {
        'lista_instructores': lista_instructor,
    }
    return HttpResponse(template.render(context, request))

def detalle_instructor(request, id_aprendiz):
    instructor_obj = instructor.objects.get(document=id_aprendiz)
    template = loader.get_template('detalle_instructor.html')
    context = {
        'instructor': instructor_obj,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
