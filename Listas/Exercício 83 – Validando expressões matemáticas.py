'''Crie um programa onde o usuário digite uma expressão qualquer que use parêntases. 
Seu aplicativo deverá analisar se a expressão passada está com os parêntasas abertos e fechados na ordem correta.'''
# Minha Resolução
expressao = []

expressao_usuario = str(input('Digite uma expressão: '))
expressao.append(expressao_usuario)
for a in expressao:
    if not ("(") in a and not (")") in a :
        print('Você não iseriu parênteses')
    elif a.count("(") == a.count(")"):
        print('Sua expressão está correta.')
    elif a.count("(") < a.count(")"):
        print('Você esqueceu de abrir os parênteses.')
    else:
        print('Voce esqueceu de fechar os parênteses.')

# Resolução da aula
expr = str(input('Digite a expressão'))
pilha = []
for sím in expr:
    # Quando o laço percorrer a expressão e encontrar um parenteses aberto ele irá adiciona-lo a lista pilha.
    if sím == '(':
        pilha.append('(')
    # Quando ele encontrar um parênteses fechado e a lista pilha tiver ao menos um elemento ele irá excluir um parêntes fechado.
    elif sím == ')':
        if len(pilha) > 0:
            pilha.pop()
        # se a lista ainda estiver vazia ele irá adicionar um parêntes fechado.
        else:
            pilha.append(')')
            break
# se a quantidade de elementos dentro da lista for igual a zero significa que todos parenteses tiveram seus respectivos pares.
if len(pilha) == 0:
    print('Sua expressão está válida!')
# caso contrário significa que algum parênteses na lista ficou sobrando.
else:
    print('Sua expressão está errada')