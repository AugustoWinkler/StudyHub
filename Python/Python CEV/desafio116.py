"""Criar um Mini Sistema Modular para Cadastro de Nome e Idade num arquivo com texto, Um Menu com 3 Opções Ver Cadastro
Cadastrar e Sair. Tudo Modularizado
"""
from colorama import Fore
from mod import modulos

modulos.tittle('Menu Principal')
while True:
    print(Fore.LIGHTYELLOW_EX + '1-', Fore.BLUE + 'Ver Pessoas Cadastradas')
    print(Fore.LIGHTYELLOW_EX + '2-', Fore.BLUE + 'Cadastrar nova Pessoa')
    print(Fore.LIGHTYELLOW_EX + '3-', Fore.BLUE + 'Sair do Sistema')
    modulos.lin()
    escolha = int(input(Fore.LIGHTYELLOW_EX + 'Sua Opção: '))
    modulos.lin()
    if escolha == 1:
        registro = modulos.recuperar_registros()
        for nome, idade in registro:
            print(f'{nome:<30} {idade:^3} anos')
    if escolha == 2:
        a = input('Nome: ')
        b = int(input('Idade: '))
        modulos.adicionar_registro(a,b)
    elif escolha == 3:
        print(Fore.RED + 'Saindo do Sistema até logo!')
        break
