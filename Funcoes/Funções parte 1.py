'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}\n')
# Programa principal
soma(8, 9)
soma(2, 1)
soma(4, 5)''' # Aqui por padrao o a receberá o primeiro valor e b o segundo.

# definindo o valor da variavel
# soma(b = 4, a = 5) - desta forma posso dizer o valor para cada variável

'''no caso acima os valores só poderão se associar as variaveis existentes, se houverem 2 apenas dois valores poderão ser associados, caso contrário ocorrerá um erro
Mas e se precisar de inderteminados valores? utilizaremos empacotamento de valores.'''

# Empacotamento 
'''def contador(* nums):
    for valor in nums:
        print(f'{valor} ', end='')
    print('FIM')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
