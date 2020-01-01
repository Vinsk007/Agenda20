from django.shortcuts import render, redirect
from core.models import Eventos #
from django.contrib.auth.decorators import login_required  #Importa o módulo de login do django (já vem pronto, só precisa fazer o set up)
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

# def index(request):
#     return redirect(request, '/Agenda20/') #Função que redireciona a página para a /Agenda20/ quando não há nada inserido, tipo: http://127.0.0.1:8000/

def login_user(request): #Adiciona função login
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request): #Adiciona função para submeter o login (com user e senha)
    if request.POST:
        username = request.POST.get('username') #POST deve ser em MAIÚSCULAS!
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválidos! Tente o Login novamente.")
    return  redirect('/')

@login_required(login_url='/login/') #decorador que inicia uma page pelo login (se não está autenticado, a page não abre)

def lista_eventos (request):
    usuario = request.user
    #eventos = Eventos.objects.get(id=1) #Pega o 1o evento da lista
    #eventos = Eventos.objects.all() #Pega todos eventos da lista
    eventos = Eventos.objects.filter(usuario=usuario) #Filtra os eventos pelo login do usuário
    #usuario = request.user
    #eventos = Eventos.objects.filter(usuario=usuario) #Pega eventos de usuário indicado
    dados = {'eventos' :eventos}
    return render(request, 'Agenda20.html', dados) #Adicionando um request da pág. Agenda20.html
#     #return HttpResponse('<h1>Hello World</h1>')
#     return HttpResponse('<h1>Endereço: {} Nro {} , {}<h1/>'.format(rua, nro, cidade)) #Passando parâmetros txt da url

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    #print(id_evento)
    dados = {}
    if id_evento:
        dados['evento'] = Eventos.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get ( 'data_evento' )
        descricao = request.POST.get ( 'descricao' )
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Eventos.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.descricao = descricao
                evento.data_evento = data_evento
                evento.save()
            #Eventos.objects.filter(id=id_evento).update(titulo=titulo,
                                                        #data_evento=data_evento,
                                                        #descricao=descricao)
        else:
            Eventos.objects.create(titulo=titulo,
                                                data_evento=data_evento,
                                                descricao=descricao,
                                                usuario=usuario)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Eventos.objects.get(id=id_evento)
    if  usuario == evento.usuario:
        evento.delete()
    return redirect('/')