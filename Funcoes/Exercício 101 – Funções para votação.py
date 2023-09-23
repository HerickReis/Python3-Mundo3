'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

# Minha rsolução
def voto(ano):
    """
    -> Realiza a verificação de idade e retorna status para votação
    :Parâmetro ano: Recebe o ano de nascimento de uma pessoa e calcula sua idade atual
    -- Programa feito por Herick com base nas aulas do Curso em video em aprendizado do Prof: Gustavo Guanabara.
    22/08/2023
    """
    from datetime import datetime

    data_atual = datetime.now()
    idade = data_atual.year - ano
    
    return idade


# Programa principal
ano_nascimento = int(input('Ano de nascimento: '))

idade_atual = voto(ano_nascimento)

if 19 <= idade_atual <= 69:
    print(f'\ncom {idade_atual} anos: VOTO OBRIGATÓRIO.')

elif 16 <= idade_atual <= 18 or idade_atual > 70:
    print(f'\nCom {idade_atual} anos: VOTO OPCIONAL.')

elif idade_atual < 16:
    print(f'\nCom {idade_atual} anos: VOTO ANULADO.')


# Resolução do curso
'''def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL.'


# Programa principal
nasc = int(input('Em que anos você nasceu? '))
print(voto(2000))'''