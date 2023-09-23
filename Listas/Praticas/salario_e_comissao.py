'''Utilize uma lista para resolver o problema a seguir. 
Uma empresa paga seus vendedores com base em comissões. 
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. 
Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.'''
# 1 - Descobrir o que diabos é uma array. (É uma variável composta como listas, tuplas etc... é uma variavel que possibilita o armazenamento de vários valores.)
# 2 - O enunciado não nos dá a comissão dos funcionários e quantos são, então teremos que criar valores hipotéticos.
# 3 - criar uma lista com os valores de venda brutas de cada vendedor.
# 4 - inicializar um loop onde irá percorrer a lista de vendas e calcular o valor semanal mais a comissão.
# 5 - Criar a fórmula para chegar a posição de salário de cada vendedor
vendas_brutas = [3000, 800, 569, 781, 2500, 4650, 621, 450, 7000]
intervalo_salarios = [200, 299, 300, 399, 400, 499, 500, 599, 600, 699, 700, 799, 800, 899, 900, 999]
contador_intervalos = [0] * (len(intervalo_salarios))

for s in vendas_brutas:
    #salario_bruto = 200 + (s * 9 / 100)
    salario_bruto = 200 + (s * 0.09)   # duas formas de calcular porcentagem :)
    # Percorre a lista de salarios em valores pares
    for i in range(0, len(intervalo_salarios), 2):
        # verifica se o salario bruto está no intervalo dos salários.
        if intervalo_salarios[i] <= salario_bruto <= intervalo_salarios[i + 1]:
            contador_intervalos[i//2] += 1

for i, valor in enumerate(intervalo_salarios):
    if i % 2 == 0:
        print(f'{valor} - {intervalo_salarios[i + 1]}:\t{contador_intervalos[i // 2]}')
