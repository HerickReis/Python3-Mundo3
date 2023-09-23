'''Escreva um programa que receba duas tuplas de coordenadas (x, y) e calcule a distância entre os pontos.'''
'''
A fórmula do Teorema de Pitágoras é dada por:
d = √((x2 - x1)^2 + (y2 - y1)^2)''' # d = distãncia
from math import sqrt
#      Coordenadas
#        y,x1 y,x2 pontos
ponto_A = (2, 3)
ponto_B = (5, 7)

distancia = sqrt((ponto_B[0] - ponto_A[0]) ** 2 + (ponto_B[1] - ponto_A[1]) ** 2)
print(f'{distancia:.3f}')
