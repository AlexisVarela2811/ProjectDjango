from django.shortcuts import render

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
    return render(request,'StoreGames/html/registro.html')

#vista para recuperar
def recuperar(request):
    return render(request,'StoreGames/html/recuperar.html')

#vista para panel_control_admi
def panel_control_admi(request):
    return render(request,'StoreGames/html/panel_control_admi.html')

#vista para ingresar contenido
def ingresarcontenido(request):
    return render(request,'StoreGames/html/ingresarcontenido.html')
