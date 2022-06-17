from django.shortcuts import render, redirect
from _datetime import datetime
#coloquei esta linha acima visando uma alternativa para corrigir o fuso horário no registro do evento. entretanto ainda não encontrei asolução.
from core.models import Evento

# Create your views here.

#def index(request):
#    return redirect('/agenda/')

def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
