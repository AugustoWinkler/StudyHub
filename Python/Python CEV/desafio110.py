#Utilizando modulos crie um modulo moeda.py  que tenha funções incorporadas aumentar(),Dimunuir(),dobro(),metade()
#Use este programa para importar esse módulo e utilizar suas funções

from uteis import moedas

p = float(input('Digite o Preço: R$'))
print(f'a metade de {p} é {moedas.metade(p)}')
print(f'o dobro de {p} é {moedas.dobro(p)}')
print(f'Aumentando 10% temos {moedas.aumentar(p,10)}')
print(f'Diminuindo 13% temos {moedas.diminuir(p,13)}')
