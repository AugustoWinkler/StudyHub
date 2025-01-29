#Objetivo Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por
# dia e R$0,15 por Km rodado.

x = int(input('Dias de uso:'))
z = int(input('Quilometros rodados:'))

d = x*60
k = z*0.15

print('Você ficou com o carro {} dias, valor {}R$ , e andou por {}km, valor: {}R$ Totalizando: {}R$'.format(x,d,z,k,z+k))