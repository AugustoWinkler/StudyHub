#Aprimore o desafio 110 com formatação de Moedas

from uteis import moedas

p = float(input('Digite o Preço: R$'))
print(f'a metade de {moedas.moedas(p)} é {moedas.moedas(moedas.metade(p))}')
print(f'o dobro de {moedas.moedas(p)} é {moedas.moedas(moedas.dobro(p))}')
print(f'Aumentando 10% temos {moedas.moedas(moedas.aumentar(p,10))}')
print(f'Diminuindo 13% temos {moedas.moedas(moedas.diminuir(p,13))}')
