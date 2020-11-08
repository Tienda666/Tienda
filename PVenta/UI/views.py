from django.shortcuts import render
from django.db import connection
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout

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
        #with connection.cursor() as cursor:
            #cursor.execute("exec miperfil1 %s", ['Tienda'])
            #datos = cursor.fetchone()
            #print(datos)
            #perfil = {'miperfil': datos}
        
        return render(request, 'profile.html')#Hacer html para mandar un mensaje de error
    else:
        return render(request, 'index.html')
def registrarventas(request):
    if request.user.is_authenticated:
        #with connection.cursor() as cursor:
            #cursor.execute("exec miperfil1 %s", ['Tienda'])
            #datos = cursor.fetchone()
            #print(datos)
            #perfil = {'miperfil': datos}
        
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
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
    return render(request, 'registrarabono.html')


 