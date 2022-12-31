from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('documento', views.documentos, name='documentos'),
    path('crear_doc', views.crear_doc, name='crear_doc'),    
    path('eliminar_doc/<int:id_doc>', views.eliminar_doc, name='eliminar_doc'),
    path('editar_doc/<int:id_doc>', views.editar_doc, name='editar_doc'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)