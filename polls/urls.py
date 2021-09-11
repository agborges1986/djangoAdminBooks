from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes', views.clientes, name='clientes'),
    path('sitios', views.sitios, name='clientes'),
    path('leads', views.leads, name='leads'),
    path('docs', views.documentos, name='documentos'),
    path('libros_publicadores', views.libros_publicadores, name='libros_publicadores'),
    path('createB', views.createB, name='createB'),
    path('getB', views.getB, name='getB'),
    path('updB', views.updB, name='updB'),
    path('delB', views.delB, name='delB'),
    path('addP', views.addP, name='addP'),
    path('createP', views.createP, name='createP'),
    path('getP', views.getP, name='getP'),
    path('updP', views.updP, name='updP'),
    path('delP', views.delP, name='delP'),
]