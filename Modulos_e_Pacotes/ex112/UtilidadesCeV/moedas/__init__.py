def aumentar(valor, aumento = float(0), formatado = False):
    acrescentado = valor + (valor * aumento / 100)
    
    return acrescentado if formatado is False else formatar(acrescentado)


def diminuir(valor, desconto = float(0), formatado = False):
    redução = valor - (valor * desconto / 100)

    return redução if formatado is False else formatar(redução)


def dobro(valor,formatado = False):
    dobrado = valor * 2

    return dobrado if formatado is False else formatar(dobrado)


def metade(valor,formatado = False):
    dividido = valor / 2

    return dividido if formatado is False else formatar(dividido)


def formatar(valor, moeda = 'R$'):
    formatado = f'{moeda}{valor:.2f}'.replace(".",",")
    return formatado

def resumo(valor, acrescimo, desconto):
    print()
    print('-' * 40)
    print(f'{"RESUMO VALOR":^40}')
    print('-' * 40)
    print(f'Preço analisado:\t{formatar(valor)}')
    print(f'Dobro do preço: \t{dobro(valor,True)}')
    print(f'Metade do preço:\t{metade(valor,True)}')
    print(f'Desconto de {desconto}%: \t{diminuir(valor,desconto,True)}')
    print(f'Aumento de {acrescimo}%: \t{aumentar(valor,acrescimo,True)}')
