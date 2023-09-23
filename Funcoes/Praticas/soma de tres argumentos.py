'''Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.'''

def soma(valor1,valor2,valor3):
    resultado = valor1 + valor2 + valor3
    print(f'A soma dos valores é: {resultado}')


soma(valor1=int(input('Digite o 1 valor: ')), valor2=int(input('Digite o 2 valor: ')), valor3=int(input('Digite o 3 valor: ')))