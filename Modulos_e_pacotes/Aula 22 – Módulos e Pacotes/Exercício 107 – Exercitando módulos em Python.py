'''Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.'''
from ex107 import moedas

moeda = float(input('Valor: R$'))
reajuste = float(input('Reajuste: '))

print(f'\nAumentando em {reajuste}% o valor é de {moedas.aumentar(moeda, reajuste)}')
print(f'Diminuindo em {reajuste}% o valor é de {moedas.diminuir(moeda, reajuste)}')
print(f'A metade de {moeda} é {moedas.metade(moeda)}')
print(f'O dobro de {moeda} é {moedas.dobro(moeda)}')
