
from colorama import Fore

def lin():
    print(Fore.LIGHTWHITE_EX + '-'*50)

def tittle(txt):
    lin()
    print(f'{txt:^50}')
    lin()

def adicionar_registro(nome, idade):
    with open('database.txt', 'a') as arquivo:
        arquivo.write(f'{nome},{idade}\n')



def recuperar_registros():
    with open('database.txt', 'r') as arquivo:
        registros = []
        for linha in arquivo:
            nome, idade = linha.strip().split(',')
            registros.append((nome, int(idade)))
        return registros