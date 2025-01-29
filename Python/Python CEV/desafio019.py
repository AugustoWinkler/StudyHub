#Objetivo faça um programa que leia 4 nomes e sorteie a ordem de apresentação

from random import shuffle

n1 = input('Primeiro nome:')
n2 = input('Segundo nome:')
n3 = input('Terceiro nome:')
n4 = input('Quarto nome:')

sorteio = list([n1,n2,n3,n4])
shuffle(sorteio)

print(sorteio)