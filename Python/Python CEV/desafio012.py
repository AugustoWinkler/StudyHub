#Faça um programa que leia o Valor de um Produto e mostre seu valor com 5% de desconto

x = float(input('Qual o Valor do produto?'))

d = 5*x/100

print('O produto custa {:.2f} e seu valor com 5% de Desconto será: {:.2f} tendo um Desconto de {:.2f}'.format(x,x-d, d))