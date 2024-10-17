from django.urls import path
from .views import cadastro_paciente

urlpatterns = [
    path('', cadastro_paciente, name='index')
    
]