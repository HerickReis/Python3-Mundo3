'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre—os em uma lista única 
mantenha separados os valoras para os ímparas. 
No Final, mostre os valores pares e ímpares em ordem crescente.'''

# Minha resolução (Infelizmente incorreta)
# Sem sort()
lista_par_impar = []
par = []
impar = []
for inserir in range(0,7+1):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        if len(par) == 0:
            par.append(numero)
        elif len(par) > 0:
            for pos in range(0,len(par)):
                if numero <= par[pos]:
                    par.insert(pos,numero)
                    break
            else:
                par.append(numero)
    else:
        if len(impar) == 0:
            impar.append(numero)
        elif len(impar) > 0:
            for pos in range(0,len(impar)):
                if numero > impar[pos]:
                    impar.insert(pos,numero)
                    break
            else:
                impar.append(numero)
lista_par_impar.append(par[:])
lista_par_impar.append(impar[:])
par.clear()
impar.clear()

print(f'''Os valores pares digitados foram: {lista_par_impar[0]}
Os valores impares digitados foram: {lista_par_impar[1]}''')


# Com sort()
lista_par_impar = []
par = []
impar = []
for inserir in range(0,7+1):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
par.sort()
impar.sort()
lista_par_impar.append(par[:])
lista_par_impar.append(impar[:])
par.clear()
impar.clear()
print(f'''Os valores pares digitados foram: {lista_par_impar[0]}
Os valores impares digitados foram: {lista_par_impar[1]}''')

# Correção
lista_par_impar = [[], []]
for inserir in range(0,7+1):
    adicionar = int(input('Digite um valor: '))
    if adicionar % 2 == 0:
        lista_par_impar[0].append(adicionar)
    else:
        lista_par_impar[1].append(adicionar)
print('-=' * 30)
lista_par_impar[0].sort()
lista_par_impar[1].sort()
print(f'Os valores pares digitados foram {lista_par_impar[0]}')
print(f'Os valores impares digitados foram {lista_par_impar[1]}')



# Resolução do curso
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram {num[0]}')
print(f'Os valores impares digitados foram {num[1]}')

