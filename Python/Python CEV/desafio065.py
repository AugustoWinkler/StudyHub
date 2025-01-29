"""
Faça um programa que leia vários números inteiros e pare quando o usuario digitar 999
no final mostre quantos números foram digitados e  a soma entre eles desconsiderando o 999
"""

numero = 0
contador = 0
acomulador = 0

while numero != 999:
    numero = (int(input('Digite um valor Inteiro: ')))
    contador+=1
    acomulador+=numero

print(contador-1, acomulador-999)