#Crie um programa que leia um número inteiro, e mostre se ele é par ou impar:

x=int(input('Digite um valor inteiro para saber se ele é par ou impar:'))

n=x%2

if n==1:
    print(f'O número: {x} é Impar')
else:
    print(f'O número: {x} é Par')