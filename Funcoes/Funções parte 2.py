# interactive help
'''help(len)''' # Aqui será exibido a documentação do elemento entre parênteses, neste caso irá informar a documentação do método len()

# Doc strings
'''def contador(i,f,p):
    """
        -> Faz uma contagem e mostra na tela.
        :parâmetro i: início da contagem.
        :parâmetro f: fim da contagem.
        :parâmetro p: passo da contagem.
        :return: sem retorno

    """

    c = i
    while c <= f:
        print(f'{c}',end='..')
        c += p
    print('FIM!')

help(contador)''' # As doc strings estão abaixo da linha de declaração, entre as 6 aspas duplas.


# Parâmetros opcionais
'''def somar(a=0, b=0, c=0):
    s = a+b+c
    print(f'A soma vale {s}')

somar(b=4, c=2)''' # Os parâmetros estão recebendo por padrão o valor 0, então se caso eu não passar valores para o parâmetro não haverá erro.


# Escopo de variáveis
'''def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 fora vale {n1}')'''# N1 possui 2 escopos, local e global, o n1 local se encontra dentro da declaração da função, o global se encontra no programa principal.
# Qual a diferença? uma variável global pode ser usada em todo o programa sem limitações, já uma variável local só pode ser utilizada dentro de onde ela foi declarada.

'''def funcao():
    global n1
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 fora vale {n1}')''' # Ao informar que o valor a ser utilizado na função será o valor global com a palavra "global" o python não criará uma nova variável e sim modificará a global


# Retorno de valores
'''def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')''' # desta forma não é possível exibir um print personalizado.


'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s''' # com o return é possível exibir um print personalizado.

'''r1 = somar(3, 2, 5) 
r2 = somar(2, 2)
r3 = somar(6)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')'''# basta que os resultados possuam variáveis, que o valor será atribuído ao valor de saída return.

# Prática

'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são: {f1}, {f2} e {f3}')'''

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par !')
else:
    print('Não é par !')
