#Objetivo fazer um programa que leia o valor de 3 retas e mostre se é possível criar um triangulo com elas

r1 = int(input('Qual o tamanho da reta 1?:'))
r2 = int(input('Qual o tamanho da reta 2?:'))
r3 = int(input('Qual o tamanho da reta 3?'))

if r1>=r2+r3:
    print('Não é possivel formar um triangulo.')
elif r2>=r1+r3:
    print('Não é possivel formar um triangulo.')
elif r3>=r1+r2:
    print('Não é possivel formar um triangulo.')
else:
    print('é possível formar um triangulo.')
