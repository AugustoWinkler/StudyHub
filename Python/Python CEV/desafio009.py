#Objetivo faça um programa que leia um número inteiro e mostre na tela sua Tabuada

x = int(input('Me Diga um Número para Obter sua Tabuada: '))

t1 = x*1
t2 = x*2
t3 = x*3
t4 = x*4
t5 = x*5
t6 = x*6
t7 = x*7
t8 = x*8
t9 = x*9
t10 = x*10

print('O Número Escolhido foi {}'.format(x))
print('{}x1 = {}\n{}x2 = {}\n{}x3 = {}\n{}x4 = {}\n{}x5 = {}\n'.format(x,t1,x,t2,x,t3,x,t4,x,t5), end='')
print('{}x6 = {}\n{}x7 = {}\n{}x8 = {}\n{}x9 = {}\n{}x10 = {}\n'.format(x,t6,x,t7,x,t8,x,t9,x,t10))