#Faça um programa que leia um ano qualquer, e mostre se ele é ou não é bissexto

x = int(input('Qual ano você quer saber se é bissexto?:'))

n = x%4

if n==0 and n%100 !=0 or n%400 ==0:
    print(f'O Ano {x} é bissexto:')
else:
    print(f'o Ano {x} não é bissexto:')