'''Crie um dicionário onde as chaves sejam nomes de frutas e os valores sejam listas contendo suas cores e quantidades disponíveis.'''
fruteira = {}
while True:
    while True:
        fruta = str(input('Fruta: ').capitalize().strip())
        if fruta not in fruteira:
            break
        print(f'{fruta} ja foi adicionada.')
    cor = str(input('Cor: ').strip().capitalize())
    quantidade = int(input('Quantidade: ').strip())
    fruteira[f'{fruta}'] = [cor,quantidade]
    while True:
        resp = str(input('\nContinuar? [S/N] ').strip()[0])
        if resp in 'SsNn':
            break
        print('\nERRO! escolha S ou N para coninuar.')
    if resp in 'Nn':
        break
    print()

while True:
    while True:
        busca = str(input('\nConsultar fruta: ').strip().capitalize())
        if busca in fruteira:
            break
        print(f'\nERRO! a fruta {busca} não foi encontrada.\n')
    print(f'A fruta {busca} tem a cor [{fruteira[busca][0]}] e possui [{fruteira[busca][1]}] unidades.')
