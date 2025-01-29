#Objetivo faça um programa que leia o nome inteiro de uma pessoa e diga se ela tem Silva no nome.

x = input('Qual seu nome inteiro?:')

nome = x.strip().upper()
validar = 'SILVA' in nome

if validar == False:
    print(f'Você não possui Silva no nome: {nome.title().split()[0]}')
else:
    print(f'Você possui Silva no nome: {nome.title().split()[0]}')