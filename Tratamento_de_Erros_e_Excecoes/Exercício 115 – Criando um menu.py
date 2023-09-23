from ex115 import menu, linha
from ex115.funcionalidades import Ver_pessoas_cadastradas, Cadastrar_nova_pessoa, verificar
import os

lista = []

verificar()

while True:
    linha.cabeçalho('MENU PRINCIPAL',40)
    resposta = menu.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Excluir pessoa cadastrada','Sair do programa'])
    
    if resposta == 1:
        Ver_pessoas_cadastradas()


    elif resposta == 2:
        while True:
            nome = str(input('Nome: ')).strip().title()
            try:
                idade = int(input('Idade: '))
            except (ValueError,TypeError):
                print(f'\033[31mERRO: Digite uma idade válida.\n\033[m')
                continue

            lista = [nome, idade]
            break
        Cadastrar_nova_pessoa(lista)
        print(f'Registro de {nome} adicionado com sucesso.')
        lista.clear()

    elif resposta == 4:
        linha.cabeçalho('Saindo do sistema... Até logo !', 40)
        break
