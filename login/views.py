from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
import global_config
# Create your views here.


def index(request):
    return render(request, 'login/index.html', {
        'church_name': global_config.church_name
    })


def signup(request):
    if request.method == 'GET':
        return render(request, 'login/signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                # Esta línea guarda los datos del usuario agregado en una cookie del navegador
                login(request, user)
                return redirect('login/home')
            except IntegrityError:
                return render(request, 'login/signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        else:
            return render(request, 'login/signup.html', {
                'form': UserCreationForm,
                'error': 'Las contraseñas no coinciden'
            })


def signin(request):
    if request.method == 'GET':
        return render(request, 'login/login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login/login.html', {
                'form': AuthenticationForm,
                'error': 'El usuario y/o la contraseña no existen'
            })


def signout(request):
    logout(request)
    return redirect('home')
