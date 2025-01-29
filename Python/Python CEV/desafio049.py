#Faça um programa que calcule a soma entre todos os números impares que são múltiplos de 3
#Encontrados no intervalo de 1 a 500.

x = 0
for c in range(1,500):
    if c%2==1 and c%3==0:
     x+=c
print(x)