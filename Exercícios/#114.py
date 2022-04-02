# Crie um código em Python que teste se o site pudim.com.br está acessível pelo computador usado.
#o programa vai basicamente testar se o computador tem acesso a internet / ao site

import urllib 
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError: 
    print('O site pudim não está acessível no moment o')
else:
    print('Tudo ok')
