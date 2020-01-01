"""Agenda20 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView #Redireciona para a page /Agenda20/


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Agenda20/', views.lista_eventos), #Adicionando o path da Agenda20.html nas urls
    path('Agenda20/lista/', views.json_lista_evento), #Adiciona lista em formato Json (Java script)
    #path('', views.index), #Redireciona para a função index, que leva para /Agenda20/ qndo vazio ' '
    path('', RedirectView.as_view(url='/Agenda20/')), #Outra forma de levar p/ page /Agenda20/, qndo vazio ' '
    path('login/', views.login_user), #Adiciona path para login quando não houver seção ativa de usuário
    path('login/submit', views.submit_login), #Adiciona ação de submit no login
    path('Agenda20/evento/', views.evento),
    path('Agenda20/evento/submit', views.submit_evento),
    path('Agenda20/evento/delete/<int:id_evento>/', views.delete_evento),
    path('logout/', views.logout_user)
]
