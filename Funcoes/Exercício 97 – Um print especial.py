'''Faça um programa que tenha uma funçáo chamada ascreva(), que receba um texto qualquar como parâmetro e mostre uma mansagem com tamanho adaptável.
Ex:
escreva('Olá, Mundo!)
Saída:
~~~~~~~~~~~~~
 Olá. Mundo!
~~~~~~~~~~~~~'''

def escreva(mensagem):
    tamanho = len(mensagem)
    print('~' * (tamanho + 4))
    print(f'{mensagem:>{tamanho + 2}}')
    print('~' * (tamanho + 4))


# Programa principal
escreva(str(input('Mensagem: ')))


# Resolução do curso

def escreve(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)

# Programa principal
escreve('Gustavo Guanabara')
escreve('Curso de Python no YouTube')
escreve('CeV')
