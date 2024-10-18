from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Pacientes
from .forms import PacientesForm
from django.http import HttpResponse
from .utils import criptografia


def cadastro_paciente(request):
    if request.method == "POST":
        formulario = PacientesForm(request.POST)

        print(formulario)

        if formulario.is_valid():
            paciente = formulario.save(
                commit=False
            )  # Cria o objeto, mas ainda não salva no banco de dados

            # Aqui aplica a criptografia na senha
            senha = formulario.cleaned_data.get("senha")
            senha_criptografada = criptografia(senha)  # Aplica a criptografia

            # Atualiza a senha criptografada no objeto do paciente
            paciente.senha = senha_criptografada

            paciente.save()  # Agora salva o paciente com a senha criptografada

            messages.success(request, "Paciente cadastrado com sucesso!")
            return redirect("home.html")  # Redireciona para outra página

            # Se o formulário não for válido, exibe os erros
        messages.error(request, "Erro ao cadastrar. Verifique os dados informados.")
        return render(
            request, "index.html", {"form": formulario}
        )  # Renderiza a página com os erros

    else:
        # Se o método não for POST, exibe o formulário vazio
        formulario = PacientesForm()
        return render(request, "index.html")


       # return render(request, "login.html")
