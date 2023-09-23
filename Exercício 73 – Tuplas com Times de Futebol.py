'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
Depois mostre:
A) apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times am ordem alfabética.
D) Em qual posição na tabela está o time corinthians.''' # originalmente seria chapecoense mas ela nao estava na tabela em 2023
# Minha Resolução
print('\nMinha resolução\n'.upper())
tabela_times = ('BOTAFOGO', 'PALMEIRAS', 'FLAMENGO', 'ATLÉTICO-MG', 'FLUMINENSE', 'GRÊMIO', 'ATHLETICO-PR', 'SÃO PAULO', 'CRUZEIRO', 'INTERNACIONAL', 
'FORTALEZA', 'RED BULL BRAGANTINO', 'SANTOS', 'CUIABÁ', 'BAHIA', 'CORINTHIANS', 'GOIÁS', 'AMÉRICA-MG', 'VASCO', 'CORITIBA')
print(f'''
{'-='*100}
Listas de times do Brasileirão: {tabela_times}\n
{'-='*100}
Os 5 primeiros colocados são: {tabela_times[0:5]}\n
{'-='*100}
Os 4 últimos colocados são: {tabela_times[-4:]}\n
{'-='*100}
Times em ordem Alfabética: {sorted(tabela_times)}\n
{'-='*100}
O Corinthians está na {tabela_times.index('CORINTHIANS')+1}ª posição''')


# Resolução do curso
print('\nResolução do curso\n'.upper())
# Obs --- a estrutura foi a mesma porém os nomes dos times eram diferentes e para evitar de escrever todos times novamente apenas copiei meu código :)
tabela_times = ('BOTAFOGO', 'PALMEIRAS', 'FLAMENGO', 'ATLÉTICO-MG', 'FLUMINENSE', 'GRÊMIO', 'ATHLETICO-PR', 'SÃO PAULO', 'CRUZEIRO', 'INTERNACIONAL', 
'FORTALEZA', 'RED BULL BRAGANTINO', 'SANTOS', 'CUIABÁ', 'BAHIA', 'CORINTHIANS', 'GOIÁS', 'AMÉRICA-MG', 'VASCO', 'CORITIBA')
print(f'''
{'-='*100}
Listas de times do Brasileirão: {tabela_times}\n
{'-='*100}
Os 5 primeiros colocados são: {tabela_times[0:5]}\n
{'-='*100}
Os 4 últimos colocados são: {tabela_times[-4:]}\n
{'-='*100}
Times em ordem Alfabética: {sorted(tabela_times)}\n
{'-='*100}
O Corinthians está na {tabela_times.index('CORINTHIANS')+1}ª posição''')