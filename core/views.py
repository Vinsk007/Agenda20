from django.shortcuts import render #, redirect
from core.models import Eventos #

# Create your views here.

# def index(request):
#     return redirect(request, '/Agenda20/') #Função que redireciona a página para a /Agenda20/ quando não há nada inserido, tipo: http://127.0.0.1:8000/

def lista_eventos (request):
    #eventos = Eventos.objects.get(id=1) #Pega o 1o evento da lista
    eventos = Eventos.objects.all() #Pega todos eventos da lista
    #usuario = request.user
    #eventos = Eventos.objects.filter(usuario=usuario) #Pega eventos de usuário indicado
    dados = {'eventos' :eventos}
    return render(request, 'Agenda20.html', dados) #Adicionando um request da pág. Agenda20.html
#     #return HttpResponse('<h1>Hello World</h1>')
#     return HttpResponse('<h1>Endereço: {} Nro {} , {}<h1/>'.format(rua, nro, cidade)) #Passando parâmetros txt da url
