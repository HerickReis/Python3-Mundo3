
def aumentar(valor, aumento = float(0), formatado = False):
    if formatado:
        formatar(valor)
    resultado = valor + (valor * aumento / 100)
    return resultado


def diminuir(valor, desconto = float(0), formatado = False):
    if formatado:
        formatar(valor)
    
    resultado = valor - (valor * desconto / 100)
    return resultado


def dobro(valor,formatado = False):
    if formatado:
        formatar(valor)
    
    resultado = valor * 2
    return resultado


def metade(valor,formatado = False):
    if formatado:
        formatar(valor)
    
    resultado = valor / 2
    return resultado


def formatar(valor):
    formatado = f'R${str(valor).replace(".",",")}'
    return formatado
