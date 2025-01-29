"""
Crie um programa que gere 5 números aleatórios e coloque em uma Tupla.
depois disso mostre a listagem dos números  e indique o Maior e o Menor valor que estão na Tupla
"""

from random import randint

numero = (randint(0,10) , randint(0,10) , randint(0,10) , randint(0,10) , randint(0,10))


print(f'Os Valores Gerados foram: {numero}')
print(f'O Menor valor é: {min(numero)}')
print(f'O Maior valor é: {max(numero)}')