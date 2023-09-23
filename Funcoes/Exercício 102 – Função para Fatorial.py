'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

# MInha resolução (Ficou incrivelmente parecido com a resolução da aula :O )
'''def fatorial(calcular = 1, show = False):
    """
    -> Cálcula o fatorial de um número
    :Parâmetro calcular: Número a ser calculado
    :Parâmetro show: (Opcional) Mostrar ou não a conta.
    :return: O fatorial de calcular
    -- Programa feito por Herick com base nas aulas do Curso em video em aprendizado do Prof: Gustavo Guanabara.
    22/08/2023
    """
    resultado = 1
    
    for c in range(calcular, 0, -1):
        resultado *= c
        if show == True:
            if c > 1:
                print(c, end=' x ')
            else:
                print(c,end=' = ')
                
    return resultado


# Programa pricipal
while True:
    numero_fatorial = int(input('\nDigite um numero: ').strip())
    resposta = str(input('Quer ver o processo de cálculo [S/N]? ').strip())

    if resposta not in 'SsNn':
        continue

    elif resposta in 'Ss':
        fatorial(calcular=numero_fatorial,show=True)
    
    else:
        fatorial(calcular=numero_fatorial)
    
    calculo = fatorial(numero_fatorial)
    print(f'{calculo}')'''

# Resolução do curso
def fatorial(n, show = False):
    f = 1
    for c in range(n, 0, - 1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# Programa principal
print(fatorial(20, show = True))
