'''Faça um programa que converta da notação de 24 horas para a notação de 12 horas. 
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. 
Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
Registre a informação A.M./P.M. como um valor A para A.M. e P para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. 
Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.'''

def conversor(hora,minutos):
    horario_convertido = {'13':1, '14':2, '15':3, '16':4, '17':5, '18':6, '19':7, '20':8, '21':9, '22':10, '23':11, '24': 12}
    print(f'{horario_convertido[str(hora)]}:{minutos}' if hora > 12 else f'{hora}:{minutos}',end=" ")

def momento(ciclo_dia):
    ciclo = {'A': 'A.M', 'P':'P.M'}
    print(ciclo[ciclo_dia])


while True:
    hora = int(input('\nHora: '))
    minuto = int(input('Minuto: '))
    conversor(hora,minuto)
    momento('P' if hora > 12 else 'A')
