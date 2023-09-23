def linha(separador = '-', quantidade = 10):
    print(separador * quantidade)


def cabeçalho(texto, alinhamento):
    linha('-', 40)
    print(f'{texto:^{alinhamento}}')
    linha('-', 40)
