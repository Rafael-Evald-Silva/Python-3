import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLErro:
    print('O site Pudim não esta acessivel.')
else:
    print('Consegui acessar o site pudim com sucesso.')
    print(site.read())
