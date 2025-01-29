#Aprimore o Desafio 111 com o parâmetro adicional nas funções para formatação das moedas.

from uteis import moedas
p = int(input('Digite um valor em R$: '))
print(f'a metade de {moedas.moeda(p)} é {moedas.metade(p,True)}')
print(f'o dobro de {moedas.moeda(p)} é {moedas.dobro(p, f=True)}')
print(f'Aumentando 10% temos {moedas.aumentar(p,10, f=True)}')
print(f'Diminuindo 13% temos {moedas.diminuir(p,13, f=True)}')
