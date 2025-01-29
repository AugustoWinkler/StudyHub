#Faça o Computador jogar Jokenpo com você
from colorama import Fore
from random import randint
from time import sleep

print(Fore.MAGENTA + """Vamos jogar JokenPo
[1] = Pedra
[2] = Papel
[3] = Tesoura""")
jogador = int(input(Fore.LIGHTYELLOW_EX + 'Opção:'))

print(Fore.BLUE + 'JO')
sleep(1)
print(Fore.MAGENTA + 'Ken')
sleep(1)
print(Fore.LIGHTBLUE_EX + 'PO')


computador = randint(1,3)

if computador==jogador:
    print(Fore.CYAN + 'Deu Empate.')
elif computador==1 and jogador==2:
    print(Fore.GREEN + 'Você me venceu, Eu Escolhi Pedra e Você Papel.')
elif computador==1 and jogador==3:
    print(Fore.RED + 'Eu venci!, Eu Escolhi Pedra e você Tesoura.')
elif computador==2 and jogador==3:
    print(Fore.GREEN + 'Você me venceu, Eu Escolhi Papel e você Tesoura.')
elif computador==2 and jogador==1:
    print(Fore.RED + 'Eu venci!, Eu Escolhi Papel e você Pedra.')
elif computador==3 and jogador==1:
    print(Fore.GREEN + 'Você me venceu, Eu Escolhi Tesoura e você Pedra.')
elif computador==3 and jogador==2:
    print(Fore.RED + 'Eu venci!, Eu Escolhi Tesoura e você Papel. ')
else:
    print(Fore.RED + 'Você Digitou uma opção inválida.')
sleep(1)
print(Fore.LIGHTWHITE_EX + 'Foi Divertido!')