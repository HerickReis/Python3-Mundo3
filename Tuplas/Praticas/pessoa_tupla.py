'''Crie uma tupla chamada pessoa com três elementos: seu nome, idade e cidade. Imprima a tupla.'''

pessoa = ('herick', 18, 'cotia',)
pessoa_formatado = ', '.join(str(n) for n in pessoa)
print(pessoa_formatado)