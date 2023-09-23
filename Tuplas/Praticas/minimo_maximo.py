'''Escreva um programa que receba uma tupla de números inteiros e retorne o valor mínimo e máximo da tupla.'''

numeros_inseridos = ()
numeros_totais = int(input('Quantos números quer mostrar? '))
mais = numeros_totais
while mais != 0:
        for _ in range(mais):
            numeros_usuario = int(input('Insira o número inteiro:  ').strip())
            numeros_inseridos += (numeros_usuario, )
        while True :   
            r = str(input('Quer mostrar mais números [S/N]? ').upper())
            print()
            if r == 'S' or r == 'N':
                break
            else:
                print('\nOpção inválida, Por favor, insira S ou N\n')
        if r == "S":
            mais = int(input('Quantos numeros quer inserir a mais? '))
        elif r == 'N':
            print(f'''\nForam inseridos {len(numeros_inseridos)} números\nO maior número inserido foi {max(numeros_inseridos)}
E o menor foi {min(numeros_inseridos)}\n''') 
            break