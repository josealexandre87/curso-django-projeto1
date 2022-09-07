from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'JOSE ALEXANDRE DA SILVA JUNIOR',
    })


def contato(request):
    return render(request, 'recipes/contato.html')


def sobre(request):
    return HttpResponse('SOBRE')
