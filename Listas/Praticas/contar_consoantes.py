'''Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.'''
letras = ['A brisa da manhã acariciava suavemente seu rosto enquanto ele caminhava pelas ruas silenciosas. Os raios dourados do sol começavam a despontar no horizonte, pintando o céu com tons de laranja e rosa. Era um novo dia cheio de promessas e possibilidades. Ele respirou fundo, sentindo a energia renovadora da aurora. Decidiu que, naquele momento, deixaria para trás as preocupações do passado e abraçaria a jornada que se desenrolava à sua frente. Com um sorriso no rosto, ele seguiu adiante, determinado a fazer cada instante contar.']
tot = 0
print(f'\nNa lista: \n{letras} \n\nforam encontradas as consoantes: \n',end='')
for v in letras:
    for c in v:
        if c in 'bcdfghjklmnpqrstvxywz':
            tot += letras.count(v)
            print(c,end=', ')
print(f'\nTotalizando {tot} consoantes')