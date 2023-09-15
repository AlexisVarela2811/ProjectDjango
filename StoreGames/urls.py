from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index_admin/', views.index_admin, name="index_admin"),
    path('aventura/', views.aventura, name="aventura"),
    path('carreras/', views.carreras, name="carreras"),
    path('deportes/', views.deportes, name="deportes"),
    path('rol/', views.rol, name="rol"),
    path('shooter/', views.shooter, name="shooter"),
    path('registro/', views.registro, name="registro"),  # Esta vista muestra el formulario de registro
   
    path('recuperar/', views.recuperar, name="recuperar"),
    path('panel_control_admi/', views.panel_control_admi, name="panel_control_admi"),
    path('login/', views.login, name="login"),
    path('ingresarcontenido/', views.ingresarcontenido, name="ingresarcontenido"),
    path('usuario_perfil/', views.perfilusuario, name="usuario_perfil")
]
