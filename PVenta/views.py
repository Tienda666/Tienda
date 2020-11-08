from django.shortcuts import render
from django.db import connection
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import Articulo, Cliente, Apartar, DetalleVenta
from django.views.decorators.csrf import csrf_protect
import json
from django.core import serializers
from django.http import JsonResponse
# Create your views here.
def listarventas(request):
    if request.user.is_authenticated:
        with connection.cursor() as cursor:
            cursor.execute("exec consultarventas")
            def dictfetchall(cursor):
                columns = [col[0] for col in cursor.description]
                return [
                    dict(zip(columns, row))
                    for row in cursor.fetchall()
                ]
            result1 = dictfetchall(cursor)
            cursor.execute("exec consultarclientes")
            result2 = dictfetchall(cursor)
            categorias1 = {'ventas': result1,'clientes': result2}
        return render(request, 'listarventas.html', categorias1)
    else:
        return render(request, 'index.html')

#Muestra la lista de las categorias
def listarcategorias(request):
    if request.user.is_authenticated:
        with connection.cursor() as cursor:
            cursor.execute("exec consultarcategorias")
            def dictfetchall(cursor):
                columns = [col[0] for col in cursor.description]
                return [
                    dict(zip(columns, row))
                    for row in cursor.fetchall()
                ]
            result = dictfetchall(cursor)
            categorias1 = {'categorias': result}
        return render(request, 'listarcategorias.html', categorias1)
    else:
        return render(request, 'index.html')
def listarcompras(request):
    if request.user.is_authenticated:
        data = {}
        articulos = {}
        user = Cliente.objects.get(nameCl = request.user)
        detalle = DetalleVenta.objects.filter(idCliente = user.idCliente)
        data = {'detalle' : detalle}
        return render(request, 'listarcompras.html', data)
    else:
        return render(request, 'index.html')

#Muestra la lista de los clientes para que la vean los administradores
def listarclientes(request):
    if request.user.is_authenticated:
        with connection.cursor() as cursor:
            cursor.execute("exec consultarclientes")
            def dictfetchall(cursor):
                columns = [col[0] for col in cursor.description]
                return [
                    dict(zip(columns, row))
                    for row in cursor.fetchall()
                ]
            result = dictfetchall(cursor)
            clientes1 = {'clientes': result}
        return render(request, 'listarclientes.html', clientes1)
    else:
        return render(request, 'index.html')

#Muestra la lista de los articulos para que la vean los administradores
def listararticulos(request):
    if request.user.is_authenticated:
        with connection.cursor() as cursor:
            cursor.execute("exec consultararticulos")
            def dictfetchall(cursor):
                columns = [col[0] for col in cursor.description]
                return [
                    dict(zip(columns, row))
                    for row in cursor.fetchall()
                ]
            result = dictfetchall(cursor)
            articulos1 = {'articulos': result}
        if request.user.is_staff:
            return render(request, 'listararticulos.html', articulos1)
        else:
            return render(request, 'inicio.html', articulos1)#Hacer html para mandar un mensaje de error
    else:
        return render(request, 'index.html')

#Muestra el perfil del usuario
def verperfil(request):
    if request.user.is_authenticated:
        articulos1 = {}
        if request.method == 'POST':
            #ar= Articulo.objects.get(pk=)
            result = Cliente.objects.get(nameCl = request.user)
            result.email = request.POST["email"]
            result.save()
            result.calle = request.POST["calle"]
            result.save()
            result.numero = request.POST["numero"]
            result.save()
            result.colonia = request.POST["colonia"]
            result.save()
            result.celular = request.POST["celular"]
            result.save()
            data= {'exito': 1}
            return JsonResponse(data)
        else:
            articulos1 = {}
            client = Cliente.objects.get(nameCl = request.user)
            apartados = Apartar.objects.filter(idCliente = client.idCliente, estado = 0)
            articulos = Articulo.objects.all()
            
            data = {'cliente': client, 'apartar': apartados, 'articulos': articulos}
            return render(request, 'profile.html', data)#Hacer html para mandar un mensaje de error
    else:
        return render(request, 'index.html')
@csrf_protect
def registrarventas(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            #ar= Articulo.objects.get(pk=)
            with connection.cursor() as cursor:
                try:
                    cursor.execute("exec consultararticulo %s", [request.POST['idAr']])
                    result = cursor.fetchone()
                    articulos1 = {'articulos': result}
                except Exception as e:
                    articulos1 = {'articulos': result}
                return JsonResponse(articulos1)
            
        else: 
            return render(request, 'registrarventas.html')#Hacer html para mandar un mensaje de error
    else:
        return render(request, 'index.html')
#Iniciar sesion
def inicio(request):
    if request.user.is_authenticated:
        with connection.cursor() as cursor:
            cursor.execute("exec consultararticulos")
            def dictfetchall(cursor):
                columns = [col[0] for col in cursor.description]
                return [
                    dict(zip(columns, row))
                    for row in cursor.fetchall()
                ]
            result = dictfetchall(cursor)
            articulos1 = {'articulos': result}
        return render(request, 'inicio.html', articulos1)
    else:
        return render(request, 'index.html')#Hacer html para mandar un mensaje de error
def categoriaHombre(request):
    if request.user.is_authenticated:
        with connection.cursor() as cursor:
            cursor.execute("exec consultararticulosHombre")
            def dictfetchall(cursor):
                columns = [col[0] for col in cursor.description]
                return [
                    dict(zip(columns, row))
                    for row in cursor.fetchall()
                ]
            result = dictfetchall(cursor)
            articulos1 = {'articulos': result}
        return render(request, 'inicio.html', articulos1)
    else:
        return render(request, 'index.html')#Hacer html para mandar un mensaje de error
def categoriaMujer(request):
    if request.user.is_authenticated:
        with connection.cursor() as cursor:
            cursor.execute("exec consultararticulosMujer")
            def dictfetchall(cursor):
                columns = [col[0] for col in cursor.description]
                return [
                    dict(zip(columns, row))
                    for row in cursor.fetchall()
                ]
            result = dictfetchall(cursor)
            articulos1 = {'articulos': result}
        return render(request, 'inicio.html', articulos1)
    else:
        return render(request, 'index.html')#Hacer html para mandar un mensaje de error

def registrararticulo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            idAr = request.POST['idAr']
            nameAr = request.POST['nameAr']
            idcat = request.POST['idcat']
            talla = request.POST['talla']
            cantidad = request.POST['cantidad']
            precio = request.POST['precio']
            descripcion = request.POST['descripcion']
            with connection.cursor() as cursor:
                cursor.execute("exec registrararticulo %s, %s, %s, %s, %s, %s, %s", [idAr, nameAr, idcat, talla, cantidad, precio, descripcion])
                cursor.execute("exec consultararticulo %s", [idAr])
                result = cursor.fetchone()
            if result is None:
                return render(request, 'registrararticulo.html')
            else:
               with connection.cursor() as cursor:
                cursor.execute("exec consultararticulos")
                def dictfetchall(cursor):
                    columns = [col[0] for col in cursor.description]
                    return [
                        dict(zip(columns, row))
                        for row in cursor.fetchall()
                    ]
                result = dictfetchall(cursor)
                articulos1 = {'articulos': result}
                return render(request, 'listararticulos.html', articulos1)
        
        else:
            return render(request, 'registrararticulo.html')
    else:
        return render(request, 'index.html')

def editararticulo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            idAr = request.POST['idAr']
            nameAr = request.POST['nameAr']
            idcat = request.POST['idcat']
            talla = request.POST['talla']
            cantidad = request.POST['cantidad']
            precio = request.POST['precio']
            descripcion = request.POST['descripcion']
            with connection.cursor() as cursor:
                cursor.execute("exec registrararticulo %s, %s, %s, %s, %s, %s, %s", [idAr, nameAr, idcat, talla, cantidad, precio, descripcion])
                cursor.execute("exec consultararticulo %s, %s", [nameAr, idAr])
                result = cursor.fetchone()
            if result is None:
                return render(request, 'registrararticulo.html')
            else:
               with connection.cursor() as cursor:
                cursor.execute("exec consultararticulos")
                def dictfetchall(cursor):
                    columns = [col[0] for col in cursor.description]
                    return [
                        dict(zip(columns, row))
                        for row in cursor.fetchall()
                    ]
                result = dictfetchall(cursor)
                articulos1 = {'articulos': result}
                return render(request, 'listararticulos.html', articulos1)
        else:
            return render(request, 'registrararticulo.html')
    else:
        return render(request, 'index.html')

#Iniciar sesion en la pagina
def login(request):
    with connection.cursor() as cursor:
            cursor.execute("exec consultararticulos")
            def dictfetchall(cursor):
                columns = [col[0] for col in cursor.description]
                return [
                    dict(zip(columns, row))
                    for row in cursor.fetchall()
                ]
            result = dictfetchall(cursor)
            articulos1 = {'articulos': result}
        
    if request.user.is_authenticated:
        return render(request, 'inicio.html', articulos1)
    else:
        if request.method == 'GET':
            return render(request, 'index.html', articulos1)
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is None:
                return render(request, 'index.html')
            else:
                auth_login(request, user)
                return render(request, 'inicio.html', articulos1)   

#Salir de la sesion
def salir(request):
    logout(request)
    return render(request, 'index.html')

#Crear un cliente 
def crearusuario(request):
    if request.user.is_authenticated:
        return render(request, 'inicio.html')
    else:
        if request.method == 'GET':
            return render(request, 'crearusuario.html')
        else:
            idCliente = request.POST['idCliente']
            idTipo = int(1)
            nameCl = request.POST['nameCl']
            apellidoP = request.POST['apellidoP']
            apellidoM = request.POST['apellidoM']
            calle = request.POST['calle']
            numero = request.POST['numero']
            colonia = request.POST['colonia']
            celular = request.POST['celular']
            puntos = int(5)
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            with connection.cursor() as cursor:
                cursor.execute("exec registrarcliente %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s", [idCliente, idTipo, nameCl, apellidoP, apellidoM, calle, numero, colonia, email, celular, puntos])
                cursor.execute("exec consultarcliente %s, %s", [nameCl, idCliente])
                result = cursor.fetchone()
            if result is None:
                return render(request, 'crearusuario.html')
            else:
                user = User.objects.create_user(username, email, password)
                return render(request, 'index.html')

def registraradmin(request):
    if request.method == 'GET':
        return render(request, 'registraradmin.html')
    else:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_superuser(username, email, password)
        if user is None:
            return render(request, 'registraradmin.html')
        else:
            return render(request, 'inicio.html')

def registrarabono(request):
    if request.method == 'GET':
        return render(request, 'registrarabono.html')
    else:
        return render(request, 'registrarabono.html')


            



 