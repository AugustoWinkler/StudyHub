#Objetivo faça um programa que leia Altura e Largura de uma parede
#Calcule sua área e o Quanto de Tinta será necessário cada litro de tinta = 2m^2

a = float(input('Qual a altura da parede?'))
l = float(input('Qual a largura da parede?'))

area = a * l

tinta = area/2

print('A area de sua parede é: {} m² e serão necessários {} Litros de Tinta. '.format(area,tinta))