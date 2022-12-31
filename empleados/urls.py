from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('',views.empleados, name='empleados'),
    path('crear_emp',views.crear_emp, name='crear_emp'),
    path('editar_emp',views.editar_emp, name='editar_emp'),
    path('eliminar_emp/<int:id_emp>',views.eliminar_emp, name='eliminar_emp'),
    path('editar_emp/<int:id_emp>',views.editar_emp, name='editar_emp')
]