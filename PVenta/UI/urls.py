from django.urls import path 
from PVenta.views import categoriaHombre, categoriaMujer, inicio, registrarventas, verperfil,  listararticulos, login, salir, crearusuario, listarclientes, listarcategorias, listarventas, registraradmin, registrarabono
urlpatterns = [
    path('index/', login, name='index'),#Formulario para iniciar sesion
    path('crearusuario/', crearusuario, name='crearusuario'),#Formulario para crear un cliente 
    path('inicio/', inicio, name='inicio'),#Muestra la pantall de inicio
    path('salir/', salir, name='salir'),#Salir de la sesion
    path('registraradmin/', registraradmin, name='registraradmin'),
    path('inicioo/', categoriaHombre, name='categoriaHombre'),
    path('inicioo0/', categoriaMujer, name='categoriaMujer'),
    path('miperfil/', verperfil, name='verperfil'),
    path('registrarventa/', registrarventas, name='registrarventas'),
    path('listarventas/', listarventas, name='listarventas'),
    path('registrarabono/', registrarabono, name='registrarabono'),
    path('listarclientes/', listarclientes, name='listarclientes'),#Muestra los clientes para los administradores
    path('listarcategorias/', listarcategorias, name='listarcategorias'),#Muestra las categorias para los adminstradores
    path('listararticulos/', listararticulos, name='listararticulos'),#Muestra los articulos en lista para los administradores
]

