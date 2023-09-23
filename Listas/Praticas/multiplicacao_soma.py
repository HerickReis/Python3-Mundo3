'''Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.'''
nmrs = []
soma = 0
multiplicacao = 1
for n in range(5):
    numero = int(input(f'Digite o {n+1}º número: '))
    nmrs.append(numero)

for i in nmrs:
    soma += i
    multiplicacao *= i
print(f'''Os números inseridos foram: {nmrs}
A soma de todos número é: {soma}
A multiplicação de todos é: {multiplicacao}''')