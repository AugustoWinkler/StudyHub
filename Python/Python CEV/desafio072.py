"""
Crie um programa que simule o funcionamento de um caixa eletrônico,
no inicio pergunte ao usuário qual será o valor a ser sacado
(número inteiro)
e o programa vai informar quantas cédulas de cada valor
serão entregues
"""
from colorama import Fore

print(Fore.MAGENTA + f'{"":=^40}\n{"BANCO WINKLER":=^40}\n{"":=^40}')

valor = int(input('Valor: '))
cinquenta = vinte = dez = um = 0

while True:
    if valor>50:
        cinquenta= valor//50
        valor-=cinquenta*50
    if valor>20:
        vinte=valor//20
        valor-=vinte*20
    if valor>10:
        dez = valor//10
        valor-=dez*10
    if valor>=1:
        um = valor
        valor-=valor
    else:
        break

if cinquenta > 0:
    print(f'Total de {cinquenta} cédulas de 50R$')
if vinte > 0:
    print(f'Total de {vinte} cédulas de 20R$')
if dez > 0:
    print(f'Total de {dez} cédulas de 10R$')
if um > 0:
    print(f'Total de {um} cédulas de 1R$')

