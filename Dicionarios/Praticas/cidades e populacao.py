'''Crie um dicionário com os nomes de algumas cidades como chaves e suas respectivas populações como valores. Em seguida, itere sobre o dicionário e imprima as informações de cada cidade.'''
infos_cidade = {}
cores = {'azul': "\033[34m",
        'limpa': "\033[m"}

print(f'{cores["azul"]}Para encerrar basta deixar a caixa cidade vazia e pressionar enter.{cores["limpa"]}')
while True:
    cidade = str(input(f'Nome de sua cidade: '))
    if not cidade:
        break
    infos_cidade[f'{cidade}'] = int(input(f'Total de habitantes de {cidade}: '))

for k,v in infos_cidade.items():
    print(f'{k} tem {v} habitantes')
