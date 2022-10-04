from re import template
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template

def hola(request):
    return HttpResponse("<h1>Buenas clase 41765</h1>")

def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f"La fecha y hora actual es {fecha_y_hora}")

def calcular_fecha_nacimiento(request, edad):
    
    fecha = datetime.now().year - edad 
       
    return HttpResponse(f"Tu fecha de nacimiento aproximada para tu {edad} años seria : {fecha}") 

def mi_temple(request):
   
    cargar_archivo = open(r"C:\proyecto CoderHouse\Primer Portfolio\templates\template.html", "r")
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context()
    
    temple_renderizado = template.render(contexto)
    
    return HttpResponse(temple_renderizado)