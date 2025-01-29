#Objetivo escreva um programa que leia um Valor em Metros e Mostre quanto ele é em Centimentros e Milimetros
x = int(input('Me Diga um Valor em Metros'))
c = x*100
m = c*10
print('{} Metros equivale a: {} Centimetros ou {} Milimetros'.format(x,c,m))