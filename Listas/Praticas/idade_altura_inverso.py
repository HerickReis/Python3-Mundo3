'''Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.'''
idade = altura = []
for info in range(5):
    print('_'*40)
    print(info+1,'ª PESSOA')
    print('_'*40)
    idade.append(int(input(f'\nIdade: ').strip()))
    altura.append(float(input(f'Altura: ')))
idade.sort(reverse=True)
altura.sort(reverse=True)
