'''Crie um dicionário que represente informações de uma pessoa (nome, idade, cidade, etc.) e imprima uma mensagem usando os valores do dicionário.'''
info_pessoa = {}
info_pessoa['nome'] = str(input('Nome: ').capitalize().strip())
info_pessoa['idade'] = int(input('Idade: '))
info_pessoa['cidade'] = str(input('Cidade: ')) 
print('Os dados informados foram: ')
for k in info_pessoa.keys():
    print(f'{k:<15}',end=' ')
print()
print('-' * 40)
for v in info_pessoa.values():
    print(f'{v:<15}',end=' ')