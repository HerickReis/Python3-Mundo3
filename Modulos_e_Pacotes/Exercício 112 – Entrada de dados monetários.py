from ex112.UtilidadesCeV import moedas
from ex112.UtilidadesCeV import dados

valor = dados.LeiaDinheiro('Digite o valor: R$')
aumento = dados.LeiaDinheiro('Aumento: ')
desconto = dados.LeiaDinheiro('Desconto: ')

moedas.resumo(valor,aumento,desconto)
