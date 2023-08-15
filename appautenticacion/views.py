from typing import Any
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import *
from django.urls import reverse_lazy
from appautenticacion.conexion import Autenticacion
from .models import *
from .forms import *

# Create your views here.

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'El nombre de Usuario o la contraseña son incorrectas')
    return render(request,'registration/login.html')

def log_out(request):
    logout(request)
    return redirect('login')

def index(request):
    return render(request, 'base.html')

class CrearServicioView(CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'servicio/crearservicioview.html'
    success_url = reverse_lazy('crearservicioview')

    def get(self, request, *args, **kwargs):
        servicios = Servicio.objects.all()
        return render(request,self.template_name,{'form':self.form_class,'servicios':servicios})

class CrearClienteView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/crearclienteview.html'
    success_url = reverse_lazy('crearclienteview')

    def get(self, request, *args, **kwargs):
        clientes = Cliente.objects.all()
        return render(request,self.template_name,{'form':self.form_class,'clientes':clientes,'tipo':'Cliente'})
    