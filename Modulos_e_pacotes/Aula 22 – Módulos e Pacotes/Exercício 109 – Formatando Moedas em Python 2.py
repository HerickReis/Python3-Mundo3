from ex109 import moedas

valor = float(input('Valor: '))
reajuste = float(input('Reajuste: '))

print(f"Aumentando {moedas.formatar(valor)} em {reajuste}% o valor fica em {moedas.aumentar(valor, reajuste, True)}")
print(f'Diminuindo {moedas.formatar(valor)} em {reajuste}% o valor fica em {moedas.diminuir(valor, reajuste, True)}')
print(f'Metade de {moedas.formatar(valor)} é {moedas.metade(valor, True)}')
print(f'O dobro de {moedas.formatar(valor)} é {moedas.dobro(valor, True)}')
