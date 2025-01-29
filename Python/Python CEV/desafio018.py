#Objetivo faça um programa que leia 4 nomes e sorteie um nome:
from random import choice

n1 = input('Qual o nome do primeiro aluno?')
n2 = input('Qual o nome do segundo aluno?')
n3 = input('Qual o nome do terceiro aluno?')
n4 = input('Qual o nome do quarto aluno?')

nomes = [n1,n2,n3,n4]

escolhido = choice(nomes)

print(f'O Nome escolhido foi: {escolhido}')

