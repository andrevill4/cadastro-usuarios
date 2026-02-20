from django.shortcuts import render, redirect
from .models import Usuario

def dashboard(request):
    total_usuarios = Usuario.objects.count()
    ultimos_usuarios = Usuario.objects.order_by('-id_usuario')[:5]

    context = {
        'total_usuarios': total_usuarios,
        'ultimos_usuarios': ultimos_usuarios
    }

    return render(request, 'usuarios/dashboard.html', context)


def home(request):
    return render(request, 'usuarios/home.html') 

def listagem_usuarios(request):

    if request.method == "POST":
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'usuarios/usuarios.html', usuarios)

def excluir_usuario(request, id):
    usuario = Usuario.objects.get(id_usuario=id)
    usuario.delete()
    return redirect('listagem_usuarios')

