from re import template
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random

from home.models import Persona

def hola(request):
    return HttpResponse("<h1>Buenas clase 41765</h1>")

def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f"La fecha y hora actual es {fecha_y_hora}")

def calcular_fecha_nacimiento(request, edad):
    
    fecha = datetime.now().year - edad 
       
    return HttpResponse(f"Tu fecha de nacimiento aproximada para tu {edad} años seria : {fecha}") 

def mi_temple(request):
   
    cargar_archivo = open(r"C:\Proyecto porfolio\templates\mi_template.html", "r")
    
    template = Template(cargar_archivo.read())
    
    cargar_archivo.close()
    
    contexto = Context()
    
    temple_renderizado = template.render(contexto)
    
    return HttpResponse(temple_renderizado)

def tu_temple(request, nombre):
        
    template = loader.get_template("tu_template.html")
    
    template_renderizado = template.render({"persona": nombre})
    
    return HttpResponse(template_renderizado)

def prueba_template(request):
    
    mi_contexto = {
        "range" : list(range(1, 11)),
        "valor_aleatorio" : random.randrange(1, 11)
                   
    }
            
    template = loader.get_template("prueba_template.html")
    
    template_renderizado = template.render(mi_contexto)
    
    return HttpResponse(template_renderizado)

def crear_persona(request, nombre, apellido):
    
    persona = Persona(nombre=nombre, apellido=apellido, edad=random.randrange(1, 99), fecha_nacimiento=datetime.now())
    persona.save()
    
    template = loader.get_template("crear_persona.html")
    
    template_renderizado = template.render({"persona": persona})
    
    return HttpResponse(template_renderizado)

def ver_personas(request):
    
    personas = Persona.objects.all()
    
    template = loader.get_template("ver_personas.html")
    
    template_renderizado = template.render({"personas": personas})
    
    return HttpResponse(template_renderizado)