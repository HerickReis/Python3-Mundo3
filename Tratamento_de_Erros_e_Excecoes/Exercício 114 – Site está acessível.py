'''Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''
# Minha resolução
'''import requests

def analisar_site_online(url):
    try:
        verificar = requests.get(url)
        if verificar.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

url = str(input('Nome do site: '))

if analisar_site_online(f'https://www.{url}'):
    print(f'O site {url} está online.')
else:
    print(f'O site {url} não está online.')'''

# Reolução do curso
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Deu erro')
else:
    print('Tudo ok')
    