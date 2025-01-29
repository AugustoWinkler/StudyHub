#Escreva um programa que faça um computador"Pensar"
#em um número entre 0 e 5 e peça para o usuario
#tentar descobrir o número do computador
#Se o usuario acertar, dizer que ele venceu

from colorama import Fore
from time import sleep
from random import randint
print(Fore.YELLOW + '=-='*10)
print(Fore.YELLOW + 'Estou pensando em número de 0 a 5')
print(Fore.YELLOW + '=-='*10)

#Gera um número aleatório de 0 a 5
computador = randint(0,5)

jogador=(int(input('Tente advinhar qual é: '))) #Jogador tenta advinhar
print(Fore.MAGENTA + 'Processando...')
sleep(2)
if jogador == computador:
    print(Fore.GREEN + 'Caramba, Você me venceu! parabéns')
else:
    print(Fore.RED + f'Você perdeu!, Eu Escolhi o número {computador}')
print('__FIM__')