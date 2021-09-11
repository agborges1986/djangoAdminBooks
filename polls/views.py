from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def index(request):
    clientes = Client.objects.all()
    context = {
        'lista_clientes': clientes,
    }

    return render(request, 'polls/home.html', context)


def clientes(request):
    clientes = Client.objects.all()
    context = {
        'lista_clientes': clientes,
    }

    return render(request, 'polls/cliente.html', context)


def sitios(request):
    sitios = Site.objects.all()
    context = {
        'lista_sitios': sitios,
    }

    return render(request, 'polls/sitios.html', context)


def leads(request):
    leads = Lead.objects.all()
    context = {
        'lista_leads': leads,
    }

    return render(request, 'polls/leads.html', context)


def documentos(request):
    documentos = Documento.objects.all()
    context = {
        'lista_documentos': documentos,
    }

    return render(request, 'polls/docs.html', context)


def libros_publicadores(request):
    libros = Libro.objects.all()
    publicadores = Publicador.objects.all()

    context = {
        'lista_libros': libros,
        'lista_publicadores': publicadores,
    }

    return render(request, 'polls/libros.html', context)


def createB(request):
    if request.POST['titulo']:
        Libro.objects.create(titulo=request.POST['titulo'])
    return redirect("libros_publicadores")


def getB(request):
    libro = Libro.objects.get(id=request.POST['id'])
    publicador=Publicador.objects.all()
    context = {
        'libro': libro,
        'publicadores': publicador,
    }
    return render(request, 'polls/editlibros.html', context)


def updB(request):
    libro = Libro.objects.get(id=request.POST['id'])
    libro.titulo = request.POST['titulo']
    libro.publicador.clear()
    publicadores=request.POST.getlist('publicadores')
    libro.publicador.set(publicadores)
    libro.save()
    print(publicadores)
    return redirect("libros_publicadores")


def delB(request):
    Libro.objects.get(id=request.POST['id']).delete()
    return redirect("libros_publicadores")


def delP(request):
    Publicador.objects.get(id=request.POST['id']).delete()
    return redirect("libros_publicadores")


def addP(request):
    libros = Libro.objects.all()
    context = {
        'lista_libros': libros
    }
    return render(request, 'polls/addP.html', context)


def createP(request):
    if request.POST['nombre']:
        Publicador.objects.create(nombre=request.POST['nombre'])
        lib = request.POST.getlist('libros')
        Publicador.objects.last().libros.set(lib)
    return redirect("libros_publicadores")


def getP(request):
    publicador = Publicador.objects.get(id=request.POST['id'])
    libros = Libro.objects.all()
    context = {
        'publicador': publicador,
        'lista_libros' : libros
    }
    return render(request, 'polls/editP.html', context)


def updP(request):
    publicador = Publicador.objects.get(id=request.POST['id'])
    publicador.nombre = request.POST['nombre']
    publicador.save()
    publicador.libros.clear()
    lib = request.POST.getlist('libros')
    publicador.libros.set(lib)
    publicador.save()
    return redirect("libros_publicadores")
