from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Usuario
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .models import Producto



def index(request):
    return render(request, 'StoreGames/index.html')

def cierresesion(request):
    return render(request, 'StoreGames/html/cierresesion.html')

def bienvenida(request):
    return render(request, 'StoreGames/html/bienvenida.html')

def index_admin(request):
    return render(request, 'StoreGames/index_admin.html')

def aventura(request):
    productos = Producto.objects.filter(categoria_id=1)
    
    context = {
        'productos': productos
    }
    return render(request, 'StoreGames/html/aventura.html', context)


def carreras(request):
    productos = Producto.objects.filter(categoria_id=3)
    
    context = {
        'productos': productos
    }
    return render(request, 'StoreGames/html/carreras.html', context)

def deportes(request):
    productos = Producto.objects.filter(categoria_id=4)
    
    context = {
        'productos': productos
    }

    return render(request, 'StoreGames/html/deportes.html', context)

def rol(request):
    productos = Producto.objects.filter(categoria_id=5)
    
    context = {
        'productos': productos
    }
    return render(request, 'StoreGames/html/rol.html',context)

def shooter(request):
    productos = Producto.objects.filter(categoria_id=2)
    
    context = {
        'productos': productos
    }

    return render(request, 'StoreGames/html/shooter.html', context)

def editar(request):
    return render(request, 'StoreGames/html/editar_perfil.html')

def loginc(request):
    return render(request, 'StoreGames/html/login.html')

def recuperar(request):
    return render(request, 'StoreGames/html/recuperar.html')

def panel_control_admi(request):
    return render(request, 'StoreGames/html/panel_control_admi.html')

def ingresarcontenido(request):
    return render(request, 'StoreGames/html/ingresarcontenido.html')


def registro(request):
    return render(request, 'StoreGames/html/registro.html')

def cambio_contra(request):
    return render(request, 'StoreGames/html/cambio_contrasena.html')

def carro_compra(request):
    return render(request, 'StoreGames/html/carrito.html')


@login_required
def editar_perfil(request):
    if request.method == 'POST':
        usuario = request.user
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        email = request.POST['email']
        nuevo_username = request.POST['usuario']

        try:
            # Verificar si el usuario o el correo ya existen
            existing_user = Usuario.objects.exclude(pk=usuario.pk).filter(username=nuevo_username).exists()
            existing_email = Usuario.objects.exclude(pk=usuario.pk).filter(email=email).exists()

            if existing_user:
                error_message = "El nombre de usuario ya está en uso. Por favor, elige otro."
            elif existing_email:
                error_message = "El correo electrónico ya está en uso. Por favor, utiliza otro."
            else:
                # Actualizar los datos del usuario
                usuario.username = nuevo_username
                usuario.nombre = nombre
                usuario.apellidos = apellidos
                usuario.email = email
                usuario.save()
                messages.success(request, 'Perfil actualizado exitosamente.')
                return redirect('index')
        except IntegrityError as e:
            error_message = "Ha ocurrido un error durante la actualización. Por favor, inténtalo nuevamente."

        messages.error(request, error_message)

    return render(request, 'StoreGames/html/editar_perfil.html')


@login_required
def cambiar_contrasena(request):
    if request.method == 'POST':
        usuario = request.user
        contrasena_antigua = request.POST['contrasena_antigua']
        nueva_contrasena = request.POST['nueva_contrasena']
        verificacion_contrasena = request.POST['verificacion_contrasena']

        try:
            # Verificar la contraseña antigua antes de cambiarla
            if usuario.check_password(contrasena_antigua):
                # Verificar si la nueva contraseña y la verificación coinciden
                if nueva_contrasena == verificacion_contrasena:
                    usuario.set_password(nueva_contrasena)
                    usuario.save()
                    update_session_auth_hash(request, usuario)  # Actualizar la sesión para evitar cierres de sesión
                    messages.success(request, 'Contraseña cambiada exitosamente.')
                    return redirect('cambiar_contrasena')
                else:
                    error_message = "Las contraseñas no coinciden."
            else:
                error_message = "La contraseña antigua no es válida."
        except IntegrityError as e:
            error_message = "Ha ocurrido un error al cambiar la contraseña. Por favor, inténtalo nuevamente."

        messages.error(request, error_message)

    return render(request, 'StoreGames/html/cambio_contrasena.html')





#VISTA DE REGISTRAR USUARIO
def registrar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        email = request.POST['correo']
        username = request.POST['user']
        password = request.POST['pass']
        
        try:
            # Verificar si el usuario o el correo ya existen
            existing_user = Usuario.objects.filter(username=username).exists()
            existing_email = Usuario.objects.filter(email=email).exists()
            
            if existing_user:
                error_message = "El nombre de usuario ya está en uso. Por favor, elige otro."
            elif existing_email:
                error_message = "El correo electrónico ya está en uso. Por favor, utiliza otro."
            else:
                
                usuario_nuevo = Usuario(
                    username=username,
                    password=password,
                    email=email,
                    nombre=nombre,
                    apellidos=apellidos,
                )
                usuario_nuevo.set_password(password)
                usuario_nuevo.save()
                # Iniciar sesión al usuario recién registrado
                login(request, usuario_nuevo)
                return redirect('bienvenida')
        except IntegrityError as e:
            error_message = "Ha ocurrido un error durante el registro. Por favor, inténtalo nuevamente."
        
        return render(request, 'StoreGames/html/registro.html', {'error_message': error_message})
    
    return render(request, 'StoreGames/html/registro.html')



#VISTA DE INICAR SESION
def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            error_message = "Nombre de usuario o contraseña incorrectos."
            return render(request, 'StoreGames/html/login.html', {'error_message': error_message})
    return render(request, 'StoreGames/html/login.html')




def carrito_compras(request):
   
    carrito = request.session.get('carrito', {})
    

    productos_en_carrito = Producto.objects.filter(idProducto__in=carrito.keys())
    
    total = 0
    for producto in productos_en_carrito:
        producto.cantidad = carrito[str(producto.idProducto)]
        producto.subtotal = producto.precioProducto * producto.cantidad
        total += producto.subtotal
    
    return render(request, 'carrito.html', {'productos_en_carrito': productos_en_carrito, 'total': total})







