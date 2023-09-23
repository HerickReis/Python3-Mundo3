from ex108 import moedas

valor = float(input('Valor: '))
reajuste = float(input('Reajuste: R$'))

print(f'Aumentando {reajuste}% em {moedas.formatar(valor)} o valor fica em {moedas.formatar(moedas.aumentar(valor,reajuste))}')
print(f'Diminuindo em {reajuste}% em {moedas.formatar(valor)} o valor fica em {moedas.formatar(moedas.diminuir(valor, reajuste))}')
print(f'Dividindo {moedas.formatar(valor)} o valor é de {moedas.formatar(moedas.metade(valor))}')
print(f'Dobrando {moedas.formatar(valor)} o valor é de {moedas.formatar(moedas.dobro(valor))}')
