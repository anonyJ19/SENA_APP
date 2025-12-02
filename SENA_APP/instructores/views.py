from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import instructor


def lista_instructores(request):
    lista_instructor = instructor.objects.all().values()
    template = loader.get_template('lista_instructores.html')
    context = {
        'lista_instructores': lista_instructor,
    }
    return HttpResponse(template.render(context, request))


def detalle_instructor(request, id_instructor):
    instructor_obj = instructor.objects.get(documento_identidad=id_instructor)
    template = loader.get_template('detalle_instructor.html')
    context = {
        'instructor': instructor_obj,
    }
    return HttpResponse(template.render(context, request))
