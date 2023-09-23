pessoas = {'nome': 'Herick', 'sexo': 'M', 'idade': 18}
'''print(pessoas['nome'])
print(pessoas['idade'])''' # Para printar cada elemento individualmente.

'''print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')''' # Como a formatação esta dentro de aspas simples o elemento deve estar dentro de aspas duplas.

'''print(pessoas.keys())''' # mostrar apenas as chaves do dicionário
'''print(pessoas.values())''' # Mostrar apenas os valores do dicionário
'''print(pessoas.items())'''  # mostra todas chaves,valores do dicionário em forma "gráfica"

'''for k, in pessoas.keys():
    print(k)''' #Loop para percorrer o dicionarios e mostrar apenas os valores das chaves.

'''for k, v in pessoas.items(): 
    print(f'{k} = {v}')''' # Loop para percorrer o dicionario e mostar chaves e valores(parecido com enumerate, que mostrava indice e valor).

'''del pessoas['sexo']''' # Deleta alguma chave da lista, neste caso a chave sexo

# Não é necessário usar um comando como append() (não funciona em dicionários), é posível adicionar/modificar diretamente.
'''pessoas['nome'] = 'Leandro''' # Altera o valor de alguma chave.
'''pessoas['peso'] = 98.5''' # adicionar chave e valor 

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])''' # Adiconar dicionários em listas, e printar cada elemento individualmente ou não(basta referenciar apenas a posição da lista ou não referenciar).

'''estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')''' # mostrar todos valores e chaves com o comando "items()", funciona de forma parecida com o enumerate.


'''estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v,end=' ')
    print()''' # Percorre a lista e mostra apenas os valores dentro do dicionário
