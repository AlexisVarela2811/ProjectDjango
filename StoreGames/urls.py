from django.urls import path
#importo
from.views import index,index_admin,aventura,carreras,deportes,rol,shooter,login,recuperar,panel_control_admi,ingresarcontenido,registro
urlpatterns = [
    path('',index,name="index"),
    path('index_admin/',index_admin,name="index_admin"),
    path('aventura/',aventura,name="aventura"),
    path('carreras/',carreras,name="carreras"),
    path('deportes/',deportes,name="deportes"),
    path('rol/',rol,name="rol"),
    path('shooter/',shooter,name="shooter"),
    path('registro/',registro,name="registro"),
    path('recuperar/',recuperar,name="recuperar"),
    path('panel_control_admi/',panel_control_admi,name="panel_control_admi"),
    path('login/',login,name="login"),
    path('ingresarcontenido/',ingresarcontenido,name="ingresarcontenido"),
    path('deportes/',deportes,name="deportes"),
    ]
