from django.shortcuts import render
from datetime import datetime

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.template import loader

from .forms import GrupoForm, MusicoForm, ConciertoForm
from .models import Grupo, Musico, Concierto

# Create your views here.

def index(request):
    lista = Concierto.objects.all()
    form = ConciertoForm()
    context = {'objects_list': lista, 'form': form, 'type': "conciertos"}
    return render(request, 'conciertos/index.html', context)

def grupos(request):
    lista = Grupo.objects.all()
    form = GrupoForm()
    context = {'objects_list': lista, 'form': form, 'type': "grupos"}
    return render(request, 'conciertos/index.html', context)

def musicos(request):
    lista = Musico.objects.all()
    form = MusicoForm()
    context = {'objects_list': lista, 'form': form, 'type': "musicos"}
    return render(request, 'conciertos/index.html', context)

def grupo(request, id=0):
    if request.method == "POST":
        form = GrupoForm(request.POST)
        if form.is_valid():
            grupo = Grupo(nombre=form.cleaned_data['nombre'], estilo=form.cleaned_data['estilo'])
            grupo.save()
            return redirect('grupo', id=grupo.id)
    else:
        grupo = get_object_or_404(Grupo, id=id)
    return render(request, 'conciertos/content.html', {'contenido': grupo})


def musico(request, id=0):
    if request.method == "POST":
        form = MusicoForm(request.POST)
        if form.is_valid():
            musico = Musico(nombre=form.cleaned_data['nombre'], instrumento=form.cleaned_data['instrumento'], grupo=form.cleaned_data['grupo'])
            musico.save()
            return redirect('musico', id=musico.id)
    else:
        musico = get_object_or_404(Musico, id=id)
    return render(request, 'conciertos/content.html', {'contenido': str(musico) + ' plays for ' + str(musico.grupo)})

def concierto(request, id=0):
    if request.method == "POST":
        form = ConciertoForm(request.POST)
        if form.is_valid():
            concierto = Concierto(fecha=datetime.combine(form.cleaned_data['fecha'], form.cleaned_data['hora']),
                            lugar=form.cleaned_data['lugar'], grupo=form.cleaned_data['grupo'])
            concierto.save()
            return redirect('concierto', id=concierto.id)
        else:
            return HttpResponse('No has introducido correctamente los datos')
    else:
        concierto = get_object_or_404(Concierto, id=id)
    return render(request, 'conciertos/content.html', {'contenido': concierto})
