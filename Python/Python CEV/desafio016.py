#Objetivo Crie um programa que leia um número real e mostre sua porção inteira
from math import trunc
x = float(input('Me diga um número:'))
a = trunc(x)

print(f'você digitou {x} e sua parte inteira é: {a}')
