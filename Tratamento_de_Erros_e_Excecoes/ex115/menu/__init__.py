from ex115.linha import linha
from time import sleep

cor = {
"vermelho" : "\033[31m",
"fim" : "\033[m",
"azul" : "\033[34m",
"amarelo": "\033[33m"
}

def LeiaInt(txt):
    while True:
        sleep(1)
        try:
            entrada = int(input(txt))

        except KeyboardInterrupt:
            print(f'{cor["vermelho"]}O usuário preferiu não digitar este número{cor["fim"]}')
            return 0

        except ValueError:
            print(f'{cor["vermelho"]}ERRO: por favor, digite uma opção válida{cor["fim"]}')

        else:
            return entrada


def menu(opcoes):
    for indices, opc in enumerate(opcoes):
        print(f'{cor["amarelo"]}{indices + 1} -{cor["fim"]} {cor["azul"]}{opc}{cor["fim"]}')
    linha('-', 40)

    while True:
        escolha_opcao = LeiaInt('Opção: ')
        print()

        if 1 <= escolha_opcao <= len(opcoes):
            return escolha_opcao
        
        else:
            print(f'{cor["vermelho"]}ERRO: por favor, digite uma opção válida{cor["fim"]}')
            break
    sleep(1)
