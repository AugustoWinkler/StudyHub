"""
Melhore o jogo da imitação em que o computador vai pensar num número de 0 a 10
Só que agora o jogador vai tentar advinhar até acertar. mostrando no final quantos palpites foram necessário
"""

from random import randint
from colorama import Fore
from time import sleep

computador = 0
jogador = None
contador=1

while computador!=jogador:
    jogador= int(input(Fore.MAGENTA + 'Estou pensando em número de 0 a 10. tente adivinhar!\n'))
    print(Fore.CYAN + f'Round: {contador}')
    contador+=1
    computador = randint(0,10)
    print(Fore.CYAN + 'Processando...')
    sleep(1)
    print(Fore.RED + f'Você perdeu! Eu pensei no número: {computador} e você no: {jogador}')
print(Fore.GREEN + f'Parabéns você venceu!, Pensamos no número {computador} e tivemos: {contador-1} Rounds.')



