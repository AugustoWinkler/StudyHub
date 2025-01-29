#Objetivo criar um programa que leia um valor em reais e mostre quantos Dolares ela pode comprar
x = float(input('Qual o valor que deseja converter em dolares?'))

#Dolar Americano 12/04/2023 Valor: 5,01R$

z = x / 5.01

print('Com {:.2f} R$ você consegue adquirir {:.2f}$ Dolares Americanos (Valor 12/04/2023)'.format(x,z))