"""
Faça um Programa que leia vários números, Mostre a tabuada um de cada vez
O programa será encerrado quando o número for negativo
"""

numero = 1

print('Caso coloque um valor negativo o programa será Interrompido.')
while True:
    numero = int(input('Digite um valor Inteiro para saber sua Tabuada'))
    if numero<0:
        break
    for c in range(1,11):
        print(f'[{c}] x [{numero}] = {c*numero}')

print('_FIM_')