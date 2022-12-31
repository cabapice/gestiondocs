from django.urls import path
from .views import crear_usuario
from . import views

urlpatterns = [

    path('', views.inicio, name='inicio'),    
    path('iniciar_sesion/',views.iniciar_sesion, name="iniciar_sesion"),
    path('crear_usuario',crear_usuario.as_view(), name="crear_usuario"),
    path('cerrar_sesion/',views.cerrar_sesion, name="cerrar_sesion"),

]