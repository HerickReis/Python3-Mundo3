'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.'''

# Minha resolução
'''def notas(info, situação = True):
    """
    -> Calcula as médias dos alunos e retorna um dicionário com as notas, médias e situação(Opcional) da turma.
    :Parâmetro info: Recebe a lista com as notas
    :Parâmetro situação: parâmetro opcional, diz se a situação deve ser exibida.
    
    -- Programa feito por Herick com base nas aulas do Curso em video em aprendizado do Prof: Gustavo Guanabara.
    24/08/2023"""

    global resp

    maior = max(info)
    menor = min(info)
    media = 0

    for v in info:
        media += v / len(info)

    resp = {"total": len(info), "maior": maior, "menor": menor, "media": media, }

    if situação:
        if media < 5:
            resp["situação"] = 'RUIM'
        if 5 <= media <= 8:
            resp["situação"] = 'RAZOÁVEL'
        if 8 <= media <= 10:
            resp["situação"] = 'BOA'
    return resp


# Programa Principal
help(notas)
resp = []

for n in range(4):
    resp.append(float(input('Nota: ')))

while True:
    opção = str(input('Quer ver a situação [S/N]? ').strip())

    if opção in 'Ss':
        opção = True
        break
    if opção in 'Nn':
        opção = ''
        break

notas(info=resp, situação=bool(opção))
print(resp)'''


# Resolução do curso
def notas(*n, sit = False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :Parâmetro n: uma ou mais notas dos alunos (aceita várias).
    :Parâmetro sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >=5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa principal
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
