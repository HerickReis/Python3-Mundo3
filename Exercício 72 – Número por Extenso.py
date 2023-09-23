'''Crie um programa que tenha uma tupla totalmante preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 a 20) e mostrá—lo por extenso.'''
print('\nMinha resolução\n'.upper())
numeros_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',  'Oito', 'Nove', 'Dez', 
                    'Onze', 'Doze','Treze','Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezeoito', 'Dezenove','Vinte')

for n in enumerate((numeros_extenso)):# O enumerate é desnecessário pois neste caso o indice já está organizado naturalmente, mas gosto da cor roxa que o tema do vscode exibe :)
    indice = int(input('Digite um número para escrever por extenso: '))

    if indice <= 20 :
        print(f'{numeros_extenso[indice]}\n')
    else:
        print('\nNumero inválido\n')
    r = str(input('Quer digitar outro número? [S/N] ').upper())
    if r == "N":
        break

# Resolução do código
print('\nResolução do curso\n'.upper())
cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',  'Oito', 'Nove', 'Dez', 
        'Onze', 'Doze','Treze','Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezeoito', 'Dezenove','Vinte')
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        break
    print('Tente novamente.', end='')
print(f'Você digitou o número {cont[núm]}')
