'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.'''

'''cores = {"verde" : "\033[1;32;42m",
        "rosa" : "\033[1;42;35m",
        "vermelho" : "\033[1;31;7m",
        "branco" : "\033[1;7;47m",
        "fim" : "\033[0;0;0m"
}

def legenda(txt, cor = "fim"):
    """
    -> Analisa os textos, formata os tamanhos dos separadores e retorna já formatado e colorido
    :Parâmetro txt: Recebe o texto do usuário
    :Parâmetro cor(opcional): irá colorir todo o texto
    -- Programa feito por Herick com base nas aulas do Curso em video em aprendizado do Prof: Gustavo Guanabara.
    25/08/2023
    """
    tam = len(txt) + 4
    print(cores[cor])
    print('~' * tam)
    print(f'{txt:>{len(txt) + 2}}  ')
    print('~' * tam)
    print(cores["fim"])

def interactivehelp(ajuda_comando):
    """
    -> Retorna a ajuda do comando desejado
    :Parâmetro ajuda_comando: irá receber o comando/ biblioteca que o usuário digitar
    """
    print(cores["branco"])
    help(ajuda_help)
    print(cores["fim"])


while True:
    legenda('SISTEMA PYHELP',"verde")
    ajuda_help = str(input("Função ou biblioteca -> "))
    if ajuda_help.lower() == 'fim':
        break
    else: 
        interactivehelp(ajuda_help)
legenda('ATÉ LOGO!', "vermelho")
'''


# Resolução do curso
from time import sleep
c = ('\033[m',      # 0 Sem cores
    '\033[0;30;41m', # 1 - vermelho
    '\033[0;30;42m', # 2 - verde
    '\033[0;30;43m', # 3 - amarelo
    '\033[0;30;44m', # 4 - azul
    '\033[0;30;45m', # 5 - Roxo
    '\033[7;30m'     # 6 - branco
    )


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'',4)
    print(c[6], end='')
    help(com)   
    print(c[0],end='')
    sleep(2)


def título(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0], end='')
    sleep(2)

# Programa principal
comando = ''
while True:
    título('SISTEMA PYHELP', 2)
    comando = str(input('Função ou Biblioteca -> '))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
título('ATÈ LOGO', 1)
