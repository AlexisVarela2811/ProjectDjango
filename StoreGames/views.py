from django.shortcuts import render, redirect
from .models import Usuario



from datetime import datetime
# Create your views here.

# vista para index principal 
def index(request):
    return render(request,'StoreGames/index.html')

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

#vista para login
def login(request):
    return render(request,'StoreGames/html/login.html')

#vista para registro
def registro(request):

    if request.method == 'POST':
        # Obtén los datos del formulario
        nombre = request.POST['nombre']
        apellido = request.POST.get('apellidos')  # Cambia a request.POST.get
        correo = request.POST['correo']
        user = request.POST['user']
        password = request.POST['pass']  # Cambia 'pass' a 'password'
        fechanacimiento = request.POST['fechanacimiento']
        direccion = request.POST['direccion']

        # Crea una instancia de Usuario y guárdala en la base de datos
        usuario = Usuario(nombre=nombre, apellidos=apellido, correo=correo, usuario=user, contrasena=password, fechanacimiento=fechanacimiento, direccion=direccion)
        usuario.save()

        # Redirige a donde desees después de registrar el usuario
        return redirect('nombre_de_la_vista')

    # Renderiza el formulario HTML en GET
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



