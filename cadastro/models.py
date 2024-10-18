from django.db import models

class Pacientes(models.Model):
    nome = models.CharField(max_length=100)
    nascimento = models.DateField()
    genero = models.CharField(max_length=50)
    cpf = models.CharField(max_length=12, unique=True)
    endereco = models.CharField(max_length=250)
    celular = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=50)
    contatoEmergencial = models.CharField(max_length=50)

    def __str__(self):
        return self.cpf