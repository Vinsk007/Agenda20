from django.contrib import admin
from core.models import  Eventos # Importação da tabela de eventos - Aula5
# Register your models here.

# Cria classe de eventos
class EventosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao') # Itens que irão aparecer na lista de eventos
    list_filter = ('usuario', ) #Adiciona um filtro por itens da lista

# Registrar entradas no arquivo Admin - Aula5
admin.site.register(Eventos, EventosAdmin) #Deve-se associar a classe EventosAdmin


