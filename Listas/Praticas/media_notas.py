'''Faça um Programa que leia 4 notas, mostre as notas e a média na tela.'''
notas = []
total = 0
for n in range(4):
    inserir_notas = float(input(f'Digite a {n+1}ª nota: '))
    total += inserir_notas
    notas.append(inserir_notas)
print(f'Foram inseridas {len(notas)} o total é de {total} a média total é: {total/len(notas)}')