from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('login/', views.login_request, name="login"),
    path('logout', LogoutView.as_view(template_name='usuarios/logout.html'), name='Logout'),
    path('perfil', views.editar_perfil, name="perfil"),
]