#Crie um programa onde 4 jogadores jogue um Dado e tenham resultados aleatórios, guarde esses resultados em um Dicionarios
#em ordem sabendo que o vencedor tirou o maior número no dado

from random import randint
from time import sleep
cont = 0

jogadores = {'jogador1':'','jogador2':'','jogador3':'','jogador4':''}
jogadores['jogador1'] = randint(1,6)
jogadores['jogador2'] = randint(1,6)
jogadores['jogador3'] = randint(1,6)
jogadores['jogador4'] = randint(1,6)

for v,k in jogadores.items():
    print(f'{v} tirou {k}')
    sleep(0.2)
for i in sorted(jogadores, key = jogadores.get, reverse=True):
    cont +=1
    print(f'{cont}° Lugar: {i} com: {jogadores[i]}')