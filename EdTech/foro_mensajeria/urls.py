from django.urls import path
from . import views

urlpatterns = [
    # Foro
    path('foro/list', views.ForoList.as_view(), name='foro-list'),
    path('posteo/<posteo_id>', views.posteo_detalle, name="posteo-detalle"),
    path('nuevo-posteo', views.ForoCreate.as_view(), name='crear-post'),
    
    # Mensajería
    path('m-recibidos', views.MensajesRecibidosList.as_view(), name="mensajes-recibidos"),
    path('m-enviados', views.MensajesEnviadosList.as_view(), name="mensajes-enviados"),
    path('mensaje/<pk>', views.MensajeDetail.as_view(), name="mensaje"),
    path('nuevo-mensaje', views.nuevo_mensaje, name="nuevo-mensaje"),
    path('re-rv/<mensaje_id>', views.reenviar_responder, name="re-rv"),
]