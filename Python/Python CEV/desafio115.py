#Crie um código em Python que teste se o site Pudim está acessivel pelo computador usado.
import urllib
import urllib.request
try:
    site1=urllib.request.urlopen('http://pudim.com.br')
except urllib.request.URLError:
    print('O Site não está acessível no momento')
else:
    print('Consegui abrir o site com sucesso!')