"""
Escreva um programa que leia um número N inteiro
e mostre os N Primeiros elementos de uma sequencia de Fibonnaci.
"""

n = int(input('Digite um número inteiro N: '))

a, b = 0, 1
contador = 0

while contador < n:
    print(a, end=' ')
    a, b = b, a + b
    contador += 1
