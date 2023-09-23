'''Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.'''

def aumentar(valor, aumento = float(0)):

    resultado = valor + (valor * aumento / 100)
    return resultado


def diminuir(valor, desconto = float(0)):

    resultado = valor - (valor * desconto / 100)
    return resultado


def dobro(valor):
    resultado = valor * 2
    return resultado


def metade(valor):
    resultado = valor / 2
    return resultado

