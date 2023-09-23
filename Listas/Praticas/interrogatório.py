'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".'''
perguntas = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?" ]
resultado = 0
for r in perguntas:
    resposta = str(input(f'{r} [S/N] ').upper().strip()[0])
    if resposta == 'S':
        resultado += 1
if resultado == 2:
    print(f'Você respondeu a {resultado} perguntas positivamente, portanto, você foi classificado como SUSPEITO.')
elif 3 <= resultado <= 4 :
    print(f'Você respondeu a {resultado} perguntas positivamente, portanto, você foi classificado como CÚMPLICE.')
elif resultado == 5:
    print(f'Você respondeu a {resultado} perguntas positivamente, portanto, você foi classificado como ASSASSINO.')
else:
    print(f'Você respondeu a {resultado} perguntas positivamente, portanto, você foi classificado como INOCENTE.')