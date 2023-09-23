'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. 
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

# Minha Resolução
cor = {
"vermelho" : "\033[31m",
"fim" : "\033[m"
}

def LeiaInt():
    while True:
        try:
            entrada = int(input('Digite um número inteiro: '))

        except KeyboardInterrupt:
            print(f'{cor["vermelho"]}O usuário preferiu não digitar este número{cor["fim"]}')
            return 0

        except ValueError:
            print(f'{cor["vermelho"]}ERRO: por favor, digite um número inteiro válido{cor["fim"]}')

        else:
            return entrada


def LeiaFloat():
    while True:
        try:
            entrada = float(input('Digite um número real: '))

        except ValueError:
            print(f'{cor["vermelho"]}ERRO: Por favor, digite um número real válido{cor["fim"]}')

        except KeyboardInterrupt:
            print(f'{cor["vermelho"]}O usuário preferiu não digitar este número{cor["fim"]}')
            return 0

        else:
            return entrada

print(f'O valor inteiro digitado foi {LeiaInt()} e o número real foi {LeiaFloat()}')


# Resolução do curso
'''def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1 = LeiaInt('Digite um inteiro: ')
n2 = LeiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado for {n1} e o real foi {n2}')'''
