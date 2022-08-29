from http.client import HTTPResponse
from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse
from django.template import Context, Template, loader

# Create your views here.

def familiar(request):
    familiar1 = Familiar (nombre = 'Agustina', edad = 26, email= 'agus@gmail.com', fecha_nac = '1996-03-10')
    familiar2 = Familiar (nombre = 'Sergio', edad = 41, email= 'sergio@gmail.com', fecha_nac = '1981-08-21')
    familiar3 = Familiar (nombre = 'Sara', edad = 54, email= 'sara@gmail.com', fecha_nac = '1968-07-28')
    familiar4 = Familiar (nombre = 'Ramón', edad = 58, email= 'ramon@gmail.com', fecha_nac = '1964-01-16')
    familiar1.save()
    familiar2.save()
    familiar3.save()
    familiar4.save()

    diccionario = {'nombre1': familiar1.nombre,'edad1': familiar1.edad, 'email1': familiar1.email, 'fecha_nac1': familiar1.fecha_nac,'nombre2': familiar2.nombre,'edad2': familiar2.edad, 'email2': familiar2.email, 'fecha_nac2': familiar2.fecha_nac, 'nombre3': familiar3.nombre,'edad3': familiar3.edad, 'email3': familiar3.email, 'fecha_nac3': familiar3.fecha_nac, 'nombre4': familiar4.nombre,'edad4': familiar4.edad, 'email4': familiar4.email, 'fecha_nac4': familiar4.fecha_nac}
    plantilla = loader.get_template('template.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

