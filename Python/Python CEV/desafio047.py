#Faça um Programa que faça uma contagem regresiva de 10 até 0 com pause de 1 segundo
from time import sleep
from colorama import Fore
import emoji

print(Fore.MAGENTA + 'Contagem Regressiva para o Ano Novo!')
for c in range (10,0 , -1 ):
    print(c)
    sleep(1)
print(emoji.emojize(Fore.MAGENTA + ('Feliz Ano Novo! :confetti_ball:'), language = 'alias'))
