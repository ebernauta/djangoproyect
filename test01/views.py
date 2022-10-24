from datetime import datetime
import re
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render


def adios(request):
    plantilla = loader.get_template('chao.html')
    
    contexto ={
        "nombre":"Alicia",
        "apellido":"Alvarez", 
        "Fecha":datetime.now(),
        "temas": ["tema 1", "tema 2", "tema 3"]
        }
   
    #enviar
    return render(request,"chao.html", contexto)



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

def calcular(request):
    
    return render(request, "calculadora.html")

def calculoGet(request):
    # Recuperacion de valores 
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    opera = request.GET['opera']
    
    #Procesamiento 
    
    resultado = 0
    
    if opera == "S":
        operacion = "Suma"
        resultado = num1 + num2
    elif opera == "R":
        operacion = "Resta"
        resultado = num1 - num2
    elif opera == "M":
        operacion = "Multiplicación"
        resultado = num1 * num2
    elif opera == "D":
        operacion = "Division"
        resultado = num1 / num2
    
    # Entrega resultado
    
    mensaje = f"La {operacion} de {str(num1)} y {str(num2)} es: {resultado}"
    
    return HttpResponse(mensaje)

def calculoPost(request):
    #Cuando es POST AGREGAR ESTO DENTRO DEL FORM HTML {% csrf_token %}
    
    # Recuperacion de valores 
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    opera = request.POST['opera']
    
    #Procesamiento 
    
    resultado = 0
    
    if opera == "S":
        operacion = "Suma"
        resultado = num1 + num2
    elif opera == "R":
        operacion = "Resta"
        resultado = num1 - num2
    elif opera == "M":
        operacion = "Multiplicación"
        resultado = num1 * num2
    elif opera == "D":
        operacion = "Division"
        resultado = num1 / num2
    
    # Entrega resultado
    
    mensaje = f"La {operacion} de {str(num1)} y {str(num2)} es: {resultado}"
    
    return HttpResponse(mensaje)
# def oldadios(request):
    
#     #Ubicar u html
#     ruta = open(r"test01\plantillas\chao.html")
#     #cargarlo
#     plantilla = Template(ruta.read())
#     ruta.close()
#     #procesar algo
#     contexto = Context({
#         "nombre":"Alicia",
#         "apellido":"Alvarez", 
#         "Fecha":datetime.now(),
#         "temas": ["tema 1", "tema 2", "tema 3"]
#         })
#     #renderizar plantila 
#     mensaje = plantilla.render(contexto)
#     #enviar
#     return HttpResponse(mensaje)

