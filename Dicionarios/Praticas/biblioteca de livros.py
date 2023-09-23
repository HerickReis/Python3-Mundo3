'''Crie um dicionário de dicionários que represente informações de livros em uma biblioteca. Cada livro deve ter um dicionário com informações como título, autor, ano de publicação, etc.'''
biblioteca = {}
while True:
    titulo = str(input('Titulo: ').title().strip())
    autor = str(input('Autor: ').capitalize().strip())
    ano = int(input('Ano de publicação: ').strip())
    biblioteca = {'titulo': titulo, 'autor': autor, 'ano': ano}
    while True:
        resp = str(input('Adicionar outro livro? [S/N] ').strip())
        if resp in 'SsNn':
            break
    if resp in 'Nn':
        break

for k,v in biblioteca.items():
    print(f'{k.capitalize()}: {v:>10}')
