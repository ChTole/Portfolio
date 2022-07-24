from django.urls import path
from . import views

urlpatterns = [
    path('foro/list', views.ForoList.as_view(), name='foro-list'),
    path('posteo/<pk>', views.ForoDetail.as_view(), name='Detail'),
    path('mensajes', views.mensajes, name="mensajes"),
]