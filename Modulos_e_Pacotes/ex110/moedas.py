
def aumentar(valor, aumento = float(0), formatado = False):
    acrescentado = valor + (valor * aumento / 100)
    if formatado:
        acrescentado = formatar(valor + (valor * aumento / 100))
    return acrescentado


def diminuir(valor, desconto = float(0), formatado = False):
    redução = valor - (valor * desconto / 100)
    if formatado:
        redução = formatar(valor - (valor * desconto / 100))
    return redução


def dobro(valor,formatado = False):
    dobrado = valor * 2
    if formatado:
        dobrado = formatar(valor * 2)
    return dobrado


def metade(valor,formatado = False):
    dividido = valor / 2
    if formatado:
        dividido = formatar(valor / 2)
    return dividido


def formatar(valor):
    formatado = f'R${str(valor).replace(".",",")}'
    return formatado


def resumo(valor, acrescimo, desconto):
    print('-' * 40)
    print(f'{"RESUMO VALOR":^40}')
    print('-' * 40)
    print(f'Preço analisado:\t{formatar(valor)}')
    print(f'Dobro do preço: \t{dobro(valor,True)}')
    print(f'Metade do preço:\t{metade(valor,True)}')
    print(f'Desconto de {desconto}%: \t{diminuir(valor,desconto,True)}')
    print(f'Aumento de {acrescimo}%: \t{aumentar(valor,desconto,True)}')