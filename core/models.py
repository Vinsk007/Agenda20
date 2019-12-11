from django.db import models
from django.contrib.auth.models import  User

# Create your models here.

# Criando novas tabelas de eventos - Projeto Agenda20 - Aula5
class Eventos(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # Insere opção de cadastrar e deletar users (opção CASCADE apaga tudo desse user)

    class Meta:
        db_table = 'evento' #Cria um options para o noma da tabela de eventos

    def __str__(self):
        return  self.titulo  # Insere o título do evento na lista de eventos (se não aparece como 'object1'

