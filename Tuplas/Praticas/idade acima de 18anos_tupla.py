'''Crie uma função que receba uma lista de tuplas contendo o nome e a idade de várias pessoas. 
A função deve retornar uma nova lista contendo apenas as pessoas cuja idade seja maior que 18 anos.'''

pessoas = ('Arenaldo', 44,
        'Ronaldo', 35,
        'Antônio', 13,
        'Josimaldo', 11,
        'Firmino', 19,
        'Jeremias', 57)
maiores_de_18 = ()
nome_pessoas = ""
for pos in range(0, len(pessoas)):
    if pos % 2 == 0:
        nome_pessoas = str(pessoas[pos])   
    else:
        idade = pessoas[pos]
        if int(idade) > 18:
            maiores_de_18 += (nome_pessoas,idade)

print(f'As pessoas com mais de 18 anos são: ')
for p in maiores_de_18:
    print(p, end='\n')

