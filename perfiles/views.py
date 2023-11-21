from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from perfiles.models import Perfiles, Candidatos

import psycopg2
import matplotlib.pyplot as plt


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        contraseña = request.POST['password']
        user = auth.authenticate(username=username, contraseña=contraseña)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Has iniciado sesion.')
            return redirect('')
        else:
            messages.error(request, 'Los datos son incorrectos')
            return redirect('login')
    return render(request, 'perfiles/login.html')

def register(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        usuario = request.POST['usuario']
        contraseña = request.POST['contraseña']
        universidad = request.POST['universidad']
        tipo=request.POST['tipo']

        user = User.objects.create_user(first_name=apellido, last_name=apellido, username=usuario, email=email, password=contraseña)
        usuario=Perfiles(user.id, nombre, apellido, usuario, email, contraseña, universidad, tipo)
        usuario.save()

        auth.login(request, user)
        messages.success(request, 'Has iniciado sesion.')
        return render(request, 'perfiles/home.html', {'usuario': usuario})
    
    else:
        return render(request, 'perfiles/register.html')

def home(request):
    return render(request, 'perfiles/home.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
    return redirect('login')

def consulta():
    db_parameters = {
    'host': 'mg-innovation2.postgres.database.azure.com',
    'database': 'innovation',
    'user': 'MG_USER_TEST_INNOV',
    'password': '2NeRJbQs*J@aOoIwlK$IBLSGH!9mMEMtqJ2rlP4pPBL4^w',
    }
    connection = psycopg2.connect(**db_parameters)
    cursor = connection.cursor()
    query = "SELECT title_or_profession, avg(salary) FROM candidates where title_or_profession='Bachiller' or title_or_profession='Ingeniero' group by title_or_profession limit 100;"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    connection.close()

    for fila in data:
        campo = Candidatos(titulo=fila[0], salario=fila[1])
        campo.save()

def salario(request):
    consulta()
    candidates = Candidatos.objects.all()
    titulo = [candidate.titulo for candidate in candidates]
    salario = [float(candidate.salario) for candidate in candidates]

    plt.bar(titulo, salario)
    plt.xlabel('Profesión')
    plt.ylabel('Salario Promedio')
    plt.title('Promedio Salarial por Profesión')
    plt.show()
    return redirect('home')
