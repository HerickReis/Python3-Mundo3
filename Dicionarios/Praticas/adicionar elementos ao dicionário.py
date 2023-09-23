'''Crie um dicionário vazio e adicione pelo menos 3 chaves-valor a ele (por exemplo, "maçã": 2, "banana": 3, "laranja": 1).'''
lista = {}
print('Você está voltando para casa e decide passar em um horti fruti, você está na sessão de frutas, quais e qunantas frutas irá levar? ')
while True:
    frutas = str(input('Qual fruta você irá levar? '))
    lista[f'{frutas}'] = int(input(f'Quantas {frutas} irá levar? '))
    while True:
        resp = str(input('Irá levar algo mais? [S/N]').upper())
        if resp in 'SN':
            break
        print('\nERRO! Insira [S] para sim e [N] para não\n')
    if resp in 'SN':
            break

print('Sua lista de compras é: ')
print(f'{"Fruta":<15}{"Quantidade":<15}')
print('-'*30)
for k,v in lista.items():
    print(f'{k:<15} {v:<15}')
