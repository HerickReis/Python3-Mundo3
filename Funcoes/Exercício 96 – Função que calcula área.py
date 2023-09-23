'''Faça um programa que tenha uma funçáo chamada área(). que raceba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

# Minha resolução
def area(base, altura):
    total = base * altura
    print(f'A area do terreno é: {total}')

# Programa Principal
area(base= float(input('Base do terreno: ')), altura=float(input(('Altura do terreno: '))))


# Resolução do curso
def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}X{comp} é de: {a}m².')

# Programa principal
print(' Controle de Terrenos ')
print('-' * 30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l,c)
