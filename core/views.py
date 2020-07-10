from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade, soma, num1, num2):
    soma = num1 + num2
    multi = num1*num2
    return HttpResponse(
        '<h1>Hello {} de {} anos de idade</h1><br>Seus números {} e {} somados são {}. Multiplicados, são {}.'
        .format(nome, idade, num1, num2, soma, multi)
    )