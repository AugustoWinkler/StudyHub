#Faça um programa que leia o nome inteiro de uma pessoa e mostre separadamente o primeiro e o último nome

x = input('Qual seu nome compleot?:')

primeiro = x.split()[0]
ultimo = x.split()[-1]

print(f'Seu Primeiro nome é: {primeiro} e seu último nome é: {ultimo}')