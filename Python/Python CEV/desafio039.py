"""
Escreva um Programa que leia 2 números inteiros quaisquer
e mostre na tela, Qual dos 2 é maior ou se são iguais
"""

n1 = int(input('Me diga um valor inteiro qualquer:'))
n2 = int(input('Me diga outro valor inteiro qualquer:'))

if n1>n2:
    print(f'{n1} é o Maior valor.')
elif n2>n1:
    print(f'{n2} é o Maior valor.')
else:
    print('Os Valores são iguais.')