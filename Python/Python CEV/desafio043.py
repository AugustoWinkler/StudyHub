"""
Complemento Desafio 36
Faça um programa que leia 3 Retas e Mostre se é possível montar um triangulo com elas
e mostre o tipo de triangulo
Equilátero = Todos os lados iguais
Isósceles = Dois lados iguais
Escaleno =  todos os lados diferentes
"""

r1 = int(input('Qual o comprimento da primeira reta?'))
r2 = int(input('Qual o comprimento da segunda reta?'))
r3 = int(input('Qual o comprimento da terceira reta?'))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1==r2 and r2==r3:
        print('é possível formar um triangulo e ele é: Equilátero')
    elif r1==r2 or r2==r3 or r1==r3:
        print('é possivel formar um triangulo e ele é: Isósceles')
    else:
        print('é possivel formar um triangulo e ele é: Escaleno')
else:
    print('Não é possível formar um triangulo com essas retas.')