'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre—os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. No Final, serão exibidos todos os valoras únicos digitados. 
em ordam crescente.'''
# 1 - Criar um lista vazia e fazer um laço para que os números sejam adicionados.
# 2 - fazer uma verificação para adicionar o número caso ele não esteja na lista, se ja estiver exibir uma mensagem de erro.
# 3 - perguntar ao usuário se deseja continuar, se não o loop será encerrado.
# 4 - Ao finalizar exibir os valores que passaram no teste e ordenálos em ordem crescente (do menor para o maior)

# Possiveis utilizações 
#sort() - irá ordenar em ordem crescente
# While True - irá criar um loop infinito até que seja interrompido com o break
# append - irá adicionar valores a lista
# if / in / else servirão para verificação

# Minha Resolução
'''from time import sleep
numeros_unicos = []

while True:
    numero = int(input('\nDigite um número para adicionar: ').strip())
    if numero in numeros_unicos:
        print('\nNúmero já existente\n')
    else:
        print('\nNúmero adicionado com sucesso...')
        numeros_unicos.append(numero)
    resposta = str(input('\nDeseja continuar? [S/N] ').strip().upper()[0])
    while resposta not in 'SN':
        print('Por favor, digite S ou N para continuar...')
        sleep(0.5)
        resposta = str(input('\nDeseja continuar? [S/N] ').strip().upper()[0])
    if resposta == 'N':
        break
print(f'\n{sorted(numeros_unicos)}')'''

# Resolução da aula:

números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
números.sort()
print(f'Você digitou os valores {números}')