'''Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.'''
idades = [15, 14, 13, 16, 14, 15, 14, 15, 13, 14, 16, 15, 13, 15, 14, 16, 13, 15, 14, 13, 16, 14, 15, 14, 13, 15, 14, 16, 15, 14]
alturas = [1.65, 1.70, 1.62, 1.68, 1.75, 1.60, 1.72, 1.68, 1.64, 1.69, 1.71, 1.67, 1.63, 1.70, 1.68, 1.66, 1.61, 1.73, 1.67, 1.65, 1.72, 1.69, 1.70, 1.68, 1.66, 1.64, 1.71, 1.67, 1.69, 1.68]
soma_alturas = 0
for m in range(0,len(alturas)):
    soma_alturas += alturas [m]
media = soma_alturas / len(alturas)

alunos_13anos_abaixo_media = 0
for a in range(len(idades)):
    idade = idades[a] # Os valores de idades na posição a, recebem o valor  do indice atual da lista idades, possibilitando o cálculo
    altura = alturas[a] # Os valores de altura na posição a, recebem o valor do indice atual da lista alturas, possibilitando o cálculo
    print(f'Idade: {idade} Altura: {altura}')
    if idade > 13 and altura < media: # se a idade atual for 13 e a altura for menor que a média, a varivel que faz o papel de contador irá receber 1
        alunos_13anos_abaixo_media += 1

print(f'''\nA media é de: {media:.2f} metros
Existem {alunos_13anos_abaixo_media} alunos com mais de 13 anos e altura abaixo da média''')
