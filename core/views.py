from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(req, nome, idade):
    return HttpResponse(f'<h1>Hello {nome}, você tem {idade} anos!</h1>')
