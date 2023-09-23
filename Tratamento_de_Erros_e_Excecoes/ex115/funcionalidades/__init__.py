

'''
'r'  -> Usado somente para ler algo
'w'  -> Usado somente para escrever algo
'r+' -> Usado para ler e escrever algo
'a'  -> Usado para acrescentar algo
'x'  -> Tenta criar um arquivo, mas lança o erro "FileExistError" caso já existente.
'''

nome_arquivo = 'registro.txt'

# Verifica se o arquivo existe ou não
def verificar():
    """
    A função realiza a verificação de existência do arquivo, caso já exista é informado caso contrário é criado.
    """
    try:
        with open(nome_arquivo, "x"):
            pass
    except(FileExistsError):
        print(f'Arquivo {nome_arquivo} já existente.')
    else:
        print(f'Arquivo {nome_arquivo} Criado com sucesso.')


def Ver_pessoas_cadastradas():
    
    try:
        # Abre o arquivo para leitura
        with open(nome_arquivo, 'r') as leitura:
            conteudo = leitura.read()

            if not conteudo:
                print('O arquivo está vazio, adicione algumas informações')
            else:
                leitura.seek(0) # Retorna ao inicio do arquivo
                for a in leitura: # Realiza a leitura de todos os dados
                    separador = a.split(';')
                    separador[1] = separador[1].replace("\n","")

                    print(f'{separador[0]:<{maior_nome()}}{separador[1]:>3} anos')
                    
    except (FileNotFoundError):
        print('\033[31mERRO: Não há pessoas cadastradas\033[m')


def Cadastrar_nova_pessoa(pessoas):
    try:
        with open(nome_arquivo, 'a') as registro:
            for p, registradas in enumerate(pessoas):
                registro.writelines(str(registradas))
                # quebra a linha após o segundo valor
                if p % 2 == 1:
                    registro.write('\n')
                else:
                    registro.write(';')
    except:
        print('Houve um erro ao cadastrar uma nova pessoa.')


def maior_nome():
    """
    A função faz a leitura e percorre o primeiro valor onde será o nome da pessoa
    :return: -> str - Retorna a quantidade de caracters do maior nome encontrado
    """
    with open(nome_arquivo,'r') as a:

        maior = 0
        for p, nome in enumerate(a):
            ler = len(nome)
            if p == 0:
                maior = ler
            else:
                if ler > maior:
                    maior = ler
        return maior
    
def LeiaInt(txt): # A função também está aqui pois não estava conseguindo importar
    from time import sleep
    while True:
        sleep(1)
        try:
            entrada = int(input(txt))

        except KeyboardInterrupt:
            print(f'\033[31mO usuário preferiu não digitar este número\033[m')
            return 0

        except ValueError:
            print(f'\033[31mERRO: por favor, digite uma opção válida\033[m')

        else:
            return entrada


def Excluir_cadastrado(nome_arquivo):
    try:
        with open(nome_arquivo, 'r+') as arquivo:
            # Salva as informações dos arquivos em uma lista
            dados = arquivo.readlines()
            # Informa os dados presentes no arquivo
            for indice ,linha  in enumerate(dados):
                print(f'{indice + 1} - {linha.replace(";"," ")}',end='')
            # qual dado o usuário vai excluir ?
            excluir = LeiaInt('\nQual deseja excluir? ') - 1

            # valida se o valor digitado pelo usuário está de acordo com os valores da lista.
            if 0 <= excluir <= len(dados):
                # Exclui o dado escolhido / faz a leitura voltar ao topo
                dados.pop(excluir)
                arquivo.seek(0)
                # Realiza as atualizações do arquivo
                arquivo.writelines(dados)
                arquivo.truncate()  # Após a remoção do arquivo na linha 111, o truncate() faz o trabalho de salvar o arquivo no tamanho atual ou seja sem ele
                                    # os dados são removidos mas o arquivo não tem seu tamanho reajustado.
                print('Dado excluído com sucesso.')

            else:
                print('Dado não ecnontrado. Nenhum dado foi removido')

    except FileNotFoundError:
        print(f'Arquivo {nome_arquivo} não encontrado')


Excluir_cadastrado(nome_arquivo)
Ver_pessoas_cadastradas()
