#Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão aritmética, e mostre os 10 Primeiros termos
termo = int(input('Qual o Primeiro termo da Progressão?'))
razao = int(input('Qual a Razão da Progressão?'))

for c in range(termo,termo+10*razao,razao):
    print(c)