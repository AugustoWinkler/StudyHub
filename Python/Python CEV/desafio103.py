#Faça um programa com uma lista chamada números e duas funções
#f1 Sorteia 5 números aleatórios
#f2 Somapar mostra a soma entre todos valores pares.

from random import randint

num = list()
soma = 0
def sorteia():
    for i in range(0,5):
        num.append(randint(1,9))
def somapar():
    global soma
    for e in num:
        if e%2 == 0:
            soma+=e
sorteia()
print(f'Sorteando 5 Valores aleatórios {num} Pronto!')
somapar()
print(f'A Soma dos números páres é: {soma}')
