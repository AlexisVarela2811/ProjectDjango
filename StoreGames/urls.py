from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('index_admin/', views.index_admin, name="index_admin"),
    path('aventura/', views.aventura, name="aventura"),
    path('bienvenida/', views.bienvenida, name="bienvenida"),
    path('cierresesion/', views.cierresesion, name="cierresesion"),
    path('carreras/', views.carreras, name="carreras"),
    path('deportes/', views.deportes, name="deportes"),
    path('rol/', views.rol, name="rol"),
    path('shooter/', views.shooter, name="shooter"),
    path('registro/', views.registro, name="registro"), 
    path('recuperar/', views.recuperar, name="recuperar"),
    path('panel_control_admi/', views.panel_control_admi, name="panel_control_admi"),
    path('logout/', auth_views.LogoutView.as_view(next_page='cierresesion'), name='logout'),
    path('ingresarcontenido/', views.ingresarcontenido, name="ingresarcontenido"),
    path('usuario_perfil/', views.perfilusuario, name="usuario_perfil"),
    path('login/', views.login_view, name='login'),
    path('ver_perfil/', views.ver_perfil, name='ver_perfil'),
    path('perfilvisualizar/', views.perfilvisualizar, name='perfilvisualizar'),
    
]
