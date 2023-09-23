'''Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 
(que não deve ser armazenado). Após esta entrada de dados, faça:
A - Mostre a quantidade de valores que foram lidos;
B - Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
C - Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
D - Calcule e mostre a soma dos valores;
E - Calcule e mostre a média dos valores;
F - Calcule e mostre a quantidade de valores acima da média calculada;
G - Calcule e mostre a quantidade de valores abaixo de sete;
H - Encerre o programa com uma mensagem;
'''
notas_inseridas = []
soma = abaixo_sete = total = 0
valor = float(input('Insira a nota (Digite -1 para encerrar): '))
soma += valor
while valor != -1:
    notas_inseridas.append(valor)
    soma += valor
    valor = float(input('Insira a nota (Digite -1 para encerrar): '))
print(f'''\nForam lidas {len(notas_inseridas)} notas.
As notas inseridas foram: ''',end='')
media = soma / len(notas_inseridas)
# Todo código do loop for é para não colocar a "," depois do último número
for m in range(0, len(notas_inseridas)-1): # Aqui o loop irá realizar a leitura dos elementos dentro da lista e irá realizar o intervalo entre 0 e a quantidade
    if m <= len(notas_inseridas): # Então se o indice "m" for menor ou igual a leitura           
        print(notas_inseridas[m],end=', ') #  irá exibir o valor de notas_inseridas no indice "m" colocando um na frente do outro e adicionando a vírgula entre os valores
else:
    print(notas_inseridas[-1],end=' ')  # caso contrário ele irá exibir o último valor sem a vírgula
print('\n A lista com notas invertidas é: ')
notas_inseridas.reverse()
for i in notas_inseridas:
    print(i)
print(f'\nA soma de todas notas inseridas é: {soma}.')
print(f'\nA média das notas inseridas é: {media:.2f}.')
for am in notas_inseridas:
    if am > media:
        total += 1
print(f'\nTiveram {total} notas acima da média.')
for abs in notas_inseridas:
    if abs < 7 :
        abaixo_sete += 1
print(f'\nTiveram {abaixo_sete} notas abaixo de 7.')
print('\nObrigado por utilizar o programa, volte sempre :D')
