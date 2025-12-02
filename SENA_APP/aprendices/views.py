from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from aprendices.models import Aprendiz

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def aprendiz(request):
    lista_aprendices = Aprendiz.objects.all()
    template = loader.get_template('lista_aprendices.html')
    context = {
        'lista_aprendices': lista_aprendices,
    }
    return HttpResponse(template.render(context, request))

def detalle_aprendiz(request, id_aprendiz):
    # Buscar usando el nombre real del campo: "documento"
    aprendiz_obj = Aprendiz.objects.get(documento=id_aprendiz)

    template = loader.get_template('detalle_aprendiz.html')
    context = {
        'aprendiz': aprendiz_obj,
    }
    return HttpResponse(template.render(context, request))
