"""
Escreva um programa que leia um número inteiro qualquer, e pessa para o usuário escolher qual será a báse
númerica para conversão
1 para Binário
2 para Octal
3 Hexa Decimal
"""

from colorama import Fore

numero = int(input(Fore.BLUE + 'Me diga um valor inteiro qualquer.'))
conversao = int(input(Fore.BLUE + 'Para qual base númerica você quer converter este valor?\n1 = Binário\n2 = Octal\n3 = Decimal'))

Binario = bin(numero)
Octal = oct(numero)
Hexa = hex(numero)

if conversao==1:
    print(f'O valor: {numero} equivale a: {Binario[2::]} em Binário')
elif conversao==2:
    print(f'O valor: {numero} equivale a: {Octal[2::]} em Octal')
elif conversao==3:
    print(f'O valor: {numero} equivale a: {Hexa[2::]} em Hexadecimal')
else:
    print(Fore.RED + 'Você não digitou uma opção de conversão válida.')