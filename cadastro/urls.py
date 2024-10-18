from django.urls import path
from .views import cadastro_paciente
from .import views

urlpatterns = [
    path('', cadastro_paciente, name='index')
  
    
]