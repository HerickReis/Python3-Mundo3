'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

print('\nMinha resolução\n'.upper())

palavras = ("gato", "casa", "felicidade", "computador", "amor", "praia", "sol", "livro", "chocolate", "musica")

for v in range(0, len(palavras)):
    vogal = ()

    for vogais in "aeiou":
        if vogais in palavras[v].lower():
            vogal += (vogais, )
            
    print(f'Na palavra {palavras[v].title()} temos {" ".join(vogal)}')

# Resolução do curso
print('\nResolução do curso\n'.upper())

palavra = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavra:
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')


# Minha resolução corrigida
print('\nMinha resolução corrigida\n'.upper())

palavras_2 = ("gato", "casa", "felicidade", "computador", "amor", "praia", "sol", "livro", "chocolate", "musica")

for p2 in palavras_2: ## desta forma cada palavra será impressa individualmente a cada iteração do loop
    print(f'\nNa palavra {p2} temos ',end = " ") 
    for letra in p2: # como cada palavra dentro da tupla é uma lista, basta criar uma variavel que será utilizada para a procura e verificar se está dentro de cada palavra
        if letra in 'aeiou':
            print(letra,end=' ')

# cada palavra dentro da tupla é uma lista de letras, e para procurar letras dentro delas como neste caso que são as vogais 
# basta procuralas dentro de cada palavra(que são listas) de forma individual.