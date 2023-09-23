'''Crie uma lista com 5 números inteiros e uma segunda lista com 3 números inteiros. 
Verifique se a segunda lista está contida na primeira e exiba o resultado na tela.'''
lista1 = []
lista2 = []

while True:
    for l1 in range(5):
        num1 = int(input(f'Digite o {l1 + 1}º número para 1º Lista: '))
        lista1.append(num1)

    for l2 in range(3):
        num2 = int(input(f'Digite o {l2 + 1}º número para 2º Lista: '))
        lista2.append(num2)

    lista1.append(lista2[:])

    if lista2 not in lista1:
        print('Desculpe, Houve um erro e não foi possivel copiar os dados. :( ')
        lista1.clear()
    else:
        print('Todos dados copiados com sucesso. :)')
        lista2.clear()
        break
    
print(lista1)
