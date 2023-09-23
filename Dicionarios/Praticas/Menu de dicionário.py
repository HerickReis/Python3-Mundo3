from time import sleep
palavras = {
'banana': '''fruto da bananeira,comestível, é um fruto anômalo, sem sementes, desenvolvido por cultura, com casca verde e, quando maduro, amarela, parda ou avermelhada, 
com polpa brancacenta ou amarelada, pastosa, doce, esp. rica em amido e potássio''',
'maçã':'o fruto da macieira, comestível',
'caipira': 'próprio de indivíduo natural ou habitante de zona rural',
'moça': 'mulher jovem. menina que entra na puberdade e que já menstrua.',
'adjacente': '1.situado em local próximo; confinante, contíguo, vizinho. 2. posto ao lado de; junto, pegado.',
'sobreposto': '1.posto em cima, superposto. 2. substantivo masculino aquilo que se põe como enfeite ou adorno sobre vestimentas, jaezes etc. (tb. us. no pl.).',
'antepassado': 'que se antepassou; já passado ou decorrido; anterior, precedente. "todos ali recordavam fatos a." 2. que viveu há muito. "referiu-se aos a. colonizadores do país"'}

while True:
    sleep(0.6)
    print('\n[1] - Significado')
    print('[2] - Remover Palavra')
    print('[3] - Adicionar palavra\n')

    while True:
        opcao = str(input('Opção: ').strip())
        if int(opcao) in range(1,4):
            break
        print('Opção inválida, escolha entre as opções 1 e 3!')

    if opcao == '1':
        while True:
            palavra = str(input('Digite a palavra: ').strip().lower())
            if palavra in palavras:
                break
            print(f'A palavra {palavra.capitalize()} não foi encontrada')
        sleep(0.6)
        print(f'\nSignificado de {palavra.capitalize()}: {palavras[f"{palavra}"]}')
    
    elif opcao == '2':
        while True:
            palavra = str(input('\nDigite a palavra: ').strip().lower())
            if palavra in palavras:
                break
            print(f'\nA palavra {palavra.capitalize()} não foi encontrada.')
        
        del palavras[f'{palavra}']
        if palavra not in palavras:
            print(f'\n{palavra.capitalize()} foi removida com sucesso!')

    elif opcao == '3':
        while True:
            palavra = str(input('Digite a palavra para adicionar: ').strip().lower())
            if palavra not in palavras:
                break
            print(f'Não é possível adicionar pois {palavra} já se encontra no dicionário.')
        palavras[f'{palavra}'] = str(input(f'Informe o significado para {palavra}: ').strip().capitalize())
