import http
from django.http import HttpResponse

def saludo(request):
    mensaje = '<h1>Hola mundo</h1>'
    return HttpResponse(mensaje)

def buenas(request, texto):
    mensaje = "Hola, hola" + texto
    return HttpResponse(mensaje)

def gracias(request, cantidad):
    cantidad = cantidad + 1000
    mensaje = "Te doy" + str(cantidad) + " gracias"
    return HttpResponse(mensaje)