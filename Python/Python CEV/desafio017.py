#faça um programa que leia o cateto oposto e o cateto adjascente de um triangulo retangulo
#calcule e mostre o comprimento da hipotenusa
from math import pow
from math import sqrt
x = float(input('Qual o Cateto adjascente?'))
y = float(input('Qual o Cateto oposto?'))

a = pow(x,2) + pow(y,2)
r =  sqrt(a)


print(f'O Cateto Adjascente sendo: {x} e o Oposto {y} a hipotenusa é {r:.2f}')