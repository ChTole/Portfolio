from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('login_e/', views.login_request_e, name="login-e"),
    path('login_d/', views.login_request_d, name="login-d"),
    path('logout', LogoutView.as_view(template_name='usuarios/logout.html'), name='Logout'),
    path('registro', views.registro_e, name="registro"),
    path('perfil', views.editar_perfil, name="perfil"),
]