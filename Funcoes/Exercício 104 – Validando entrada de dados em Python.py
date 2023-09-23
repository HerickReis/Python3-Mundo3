'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')'''

# Minha resolução
'''def LeiaInt(entrada = ''):
    """-- Programa feito por Herick com base nas aulas do Curso em video em aprendizado do Prof: Gustavo Guanabara.
    23/08/2023"""
    
    global n
    n = 0

    while True:
        valor_entrada = input(entrada).strip()

        if n == valor_entrada:
            return n
        
        if not valor_entrada or valor_entrada.isalpha() == True:
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue

        n = valor_entrada


# Peograma principal
n = LeiaInt('Digite um número: ')
print(f'Você acabou de digitar o valor {n}')'''



# Resolução do curso
def LeiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Programa principal
n = LeiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
