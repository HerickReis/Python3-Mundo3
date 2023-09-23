'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os am uma lista, já na posiÇão correta da inserção
(sem usar o sort()) No Final, mostre a lista ordenada na tela.'''
# 1 - criar uma lista vazia para receber os valores
# 2 - loop for para percorrer 5 vezes
# 3 - verificar se o número é maior ou menor que os anteriores

# Minha Resolução
numeros = []
cont = 0
while cont < 5:
    adicionar_numero = int(input('Digite um valor: '))
    cont += 1
    # Verifica se o valor é o primeiro a ser digitado, ou se ele é maior que último valor da lista
    if len(numeros) == 0 or adicionar_numero > numeros[-1]:
        numeros.append(adicionar_numero)
        print('Adicionado ao fim da lista...')
    else:
        #verifica se o valor digitado é menor que o valor do índice atual em que o loop está percorrendo.
        for indice in range(len(numeros)):
            if adicionar_numero <= numeros[indice]:
                numeros.insert(indice,adicionar_numero)
                print(f'Adicionado a posição {indice} da lista')
                break
print(numeros)

# Resolução da aula
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adiconado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
