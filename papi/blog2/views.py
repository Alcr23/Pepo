from urllib import request
from django.shortcuts import render

#from suma import suma
from .models import Datos
# Create your views here.

def muestra_datos(request):
    consulta = Datos.objects.all()
    listaSuma=calculaSuma(consulta)
    contexto = {'Datos' : consulta, 'suma':listaSuma}
    return render(request, 'blog2/blog2.html',contexto)

def calculaSuma(l):
        listaSuma=[]
        for i in l:
            r=i.x1 + i.x3 + i.x4
            listaSuma.append(r)
        return listaSuma