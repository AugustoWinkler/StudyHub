#Faça um mini-sistema que utilize o interactive help do Python, o usuário vai digitar o comando e o manual vai aparecer
#quando o usuario digitar a palavara 'FIM' o Programa se encerra OBS use Cores.
import colorama
from time import sleep


def tittle(txt):
    tam = len(txt)
    print(colorama.Back.GREEN + colorama.Fore.LIGHTWHITE_EX +  '~'*(tam+4))
    print(f'` {txt}')
    print('~'*(tam+4))


def acessarmanual(txt):
    tam = len(txt)
    print(colorama.Back.BLUE + colorama.Fore.LIGHTWHITE_EX + '~' * (tam + 4))
    print(f'` {txt}')
    print('~' * (tam + 4))
    sleep(0.5)


def manual(txt):
    print(colorama.Back.LIGHTWHITE_EX + colorama.Fore.BLACK)
    help(txt)


def adeus(txt):
    tam = len(txt)
    print(colorama.Back.RED + colorama.Fore.LIGHTWHITE_EX + '~' * (tam + 4))
    print(f'` {txt}')
    print('~' * (tam + 4))


while True:
    tittle('Sistema de ajuda PyHelp')
    x = input(colorama.Back.RESET + 'Função ou Blibioteca >')
    if x == 'FIM':
        adeus('Até Logo!')
        break

    acessarmanual(f"Acessando Manual do Comando: '{x}'")
    manual(x)



