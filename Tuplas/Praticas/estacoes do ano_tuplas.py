'''Crie uma tupla com as estações do ano e verifique se "Verão" está presente nela.'''

estacoes = ('Outono', 'Inverno', 'Primavera','Verao')
procura = estacoes.index('Verao') if 'Verao' in estacoes else None

print('Verão está na lista' if procura is not None else 'verao não está na lista' )