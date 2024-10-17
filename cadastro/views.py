from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Pacientes
from .forms import PacientesForm


def cadastro_paciente(request):
    if request.method == "POST": 
        formulario = PacientesForm(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return render(request,'index.html')
        
    return render(request, 'index.html')