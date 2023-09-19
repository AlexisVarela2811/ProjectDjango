from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.db import IntegrityError 
from django.contrib.auth import login


from datetime import datetime
# Create your views here.

# vista para index principal 
def index(request):
    return render(request,'StoreGames/index.html')

# vista de cierre sesion
def cierresesion(request):
    return render(request,'StoreGames/html/cierresesion.html')

# vista de cierre sesion
def bienvenida(request):
    return render(request,'StoreGames/html/bienvenida.html')
    

#vista para index admin
def index_admin(request):
    return render(request,'StoreGames/index_admin.html')

#vista para aventura
def aventura(request):
    return render(request,'StoreGames/html/aventura.html')

#vista para carreras
def carreras(request):
    return render(request,'StoreGames/html/carreras.html')

#vista para deportes
def deportes(request):
    return render(request,'StoreGames/html/deportes.html')

#vista para rol
def rol(request):
    return render(request,'StoreGames/html/rol.html')

#vista para shooter
def shooter(request):
    return render(request,'StoreGames/html/shooter.html')



#vista para registro
def registro(request):
    if request.method == 'POST':
        # Obtén los datos del formulario
        nombre = request.POST['nombre']
        apellido = request.POST.get('apellidos')
        correo = request.POST['correo']
        user = request.POST['user']
        password = request.POST['pass']
        fechanacimiento = request.POST['fechanacimiento']
        direccion = request.POST['direccion']

        # Verificar si ya existe un usuario con el mismo correo o nombre de usuario
        if User.objects.filter(email=correo).exists() or User.objects.filter(username=user).exists():
            error_message = "Usuario y/o correo ya registrados."
            return render(request, 'StoreGames/html/registro.html', {'error_message': error_message})

        # Si no existe un usuario con el mismo correo o nombre de usuario, crea uno nuevo
        nuevo_usuario = User.objects.create_user(username=user, email=correo, password=password)
        nuevo_usuario.first_name = nombre
        nuevo_usuario.last_name = apellido
        nuevo_usuario.save()

        # Iniciar sesión al usuario recién registrado
        login(request, nuevo_usuario)

     
        return redirect('bienvenida')

    return render(request, 'StoreGames/html/registro.html')



#vista para recuperar
def recuperar(request):
    return render(request,'StoreGames/html/recuperar.html')

#vista para panel_control_admi
def panel_control_admi(request):
    return render(request,'StoreGames/html/panel_control_admi.html')

#vista para ingresar contenido
def ingresarcontenido(request):
    return render(request,'StoreGames/html/ingresarcontenido.html')

def perfilusuario(request):
    return render(request,'StoreGames/html/usuario_perfil.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Intenta autenticar al usuario por nombre de usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            return redirect('index')  
        else:
            error_message = "Nombre de usuario o contraseña incorrectos."
            return render(request, 'StoreGames/html/login.html', {'error_message': error_message})

    return render(request, 'StoreGames/html/login.html')
