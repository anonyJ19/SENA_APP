from django.template import loader
from django.http import HttpResponse
from .models import Programa  # Modelo programas

# Vista lista de programas
def lista_programas(request):
    lista_programas = Programa.objects.all()
    template = loader.get_template('lista_programas.html')

    context = {
        'lista_programas': lista_programas,
        'total_programas': lista_programas.count(),
    }
    return HttpResponse(template.render(context, request))

# Vista detalle de programa
def detalle_programa(request, id_programa):
    programa_obj = Programa.objects.get(codigo=id_programa)
    template = loader.get_template('detalle_programa.htm')

    context = {
        'programa': programa_obj,
    }
    return HttpResponse(template.render(context, request))
