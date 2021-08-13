from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(req, nome, idade):
    return HttpResponse(f'<h1>Hello {nome}, você tem {idade} anos!</h1>')


def soma(req, num1, num2):
    resp = num1 + num2
    return HttpResponse(f'<h1>Soma</h1><br /><h2>Resultado da soma: {resp}</h2>')


def subtracao(req, num1, num2):
    resp = num1 - num2
    return HttpResponse(f'<h1>Subtracão</h1><br /><h2>Resultado da subtracão: {resp}</h2>')


def divisao(req, num1, num2):
    resp = num1 / num2
    return HttpResponse(f'<h1>Divisão</h1><br /><h2>Resultado da divisão: {resp}</h2>')


def multiplicacao(req, num1, num2):
    resp = num1 * num2
    return HttpResponse(f'<h1>Multiplicacão</h1><br /><h2>Resultado da multiplicacão: {resp}</h2>')
