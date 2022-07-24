from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group

from .forms import *

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(dni = usuario, password = contra)            
            if user is not None:
                login(request, user)
                if user.tipo_usuario != 2:
                    return redirect('inicio')
                else:
                    # return redirect('../../docentes/docente')
                    return redirect('../../docentes/docente/' + str(user.id))
            else:
                return redirect('sitio1/inicio')
        else:
            return redirect('login')
    form = AuthenticationForm()
    ctx = {"form": form}
    return render(request, "usuarios/login.html", ctx)  

def registro_e(request):
    if request.method=="POST":
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.tipo_usuario = 1
            form.save()
            grupo = Group.objects.get(name='Estudiantes') 
            grupo.user_set.add(new_user.id)
            return redirect('index')    
    else:
        form = UsuarioCreationForm()
    return render(request,"usuarios/registro.html", {"form": form})

def editar_perfil(request):
    pass