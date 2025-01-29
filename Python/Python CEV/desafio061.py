"""
Faça um programa que leia um número qualquer e mostre seu Fatorial.
"""

numero = int(input('Digite um valor inteiro:'))
fatorial=numero-1

if numero<0:
    print('O Fatorial não está definido para números negativos')
elif numero==0:
    print('O fatorial de 0 é 1')
else:
    while fatorial!=0:
        fatorial-=1
        numero+=numero*fatorial
print(numero)
