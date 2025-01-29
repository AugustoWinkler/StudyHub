#Crie um programa com a função leiaint()
#que vai funcionar semelhante a função input() do python só que fazendo a validação  para aceitar apenas um valor númerico

from colorama import Fore


def leiaint():

    while True:
        x = input(Fore.LIGHTWHITE_EX + 'Digite um Número: ')

        if (x.isnumeric()) == False:
            print(Fore.RED + 'Erro Digite um valor Válido.')
        else:
            print(Fore.GREEN + f'Parabéns {x} é um Número.')
            break
print(leiaint())