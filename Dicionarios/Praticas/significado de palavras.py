'''Crie um dicionário com palavras e seus significados. Peça ao usuário para digitar uma palavra e verifique se a palavra está no dicionário. 
Se estiver, imprima o significado, caso contrário, exiba uma mensagem informando que a palavra não está no dicionário.'''

palavras = {
'banana': '''fruto da bananeira,comestível, é um fruto anômalo, sem sementes, desenvolvido por cultura, com casca verde e, quando maduro, amarela, parda ou avermelhada, com polpa brancacenta ou amarelada, pastosa, doce, 
esp. rica em amido e potássio''',
'maçã':'o fruto da macieira, comestível',
'caipira': 'próprio de indivíduo natural ou habitante de zona rural',
'moça': 'mulher jovem. menina que entra na puberdade e que já menstrua.',
'adjacente': '1.situado em local próximo; confinante, contíguo, vizinho. 2. posto ao lado de; junto, pegado.',
'sobreposto': '1.posto em cima, superposto. 2. substantivo masculino aquilo que se põe como enfeite ou adorno sobre vestimentas, jaezes etc. (tb. us. no pl.).',
'antepassado': 'que se antepassou; já passado ou decorrido; anterior, precedente. "todos ali recordavam fatos a." 2. que viveu há muito. "referiu-se aos a. colonizadores do país"'}

while True:
        palavra = str(input('\nQual palavra deseja procurar? '))
        while palavra not in palavras:
                print(f'\nA palavra: {palavra} não foi encontrada')
                palavra = str(input('\nQual palavra deseja procurar? '))
                print(f'{palavra}: {palavras[f"{palavra}"]}')
