from django.urls import path
from . import views

urlpatterns = [
    path('foro/list', views.ForoList.as_view(), name='foro-list'),
    path('posteo/<pk>', views.ForoDetail.as_view(), name='Detail'),
    path('m-recibidos', views.MensajesRecibidosList.as_view(), name="mensajes-recibidos"),
    path('m-enviados', views.MensajesEnviadosList.as_view(), name="mensajes-enviados"),
    path('mensaje/<pk>', views.MensajeDetail.as_view(), name="mensaje"),
    path('nuevo-mensaje', views.nuevo_mensaje, name="nuevo-mensaje"),
    path('re-rv/<mensaje_id>', views.reenviar_responder, name="re-rv"),
]