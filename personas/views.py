from django.shortcuts import render


def listar_personas(request):
    return render(request, 'personas/listar_personas.html')


def crear_persona(request):
    return render(request, 'personas/crear_persona.html')
