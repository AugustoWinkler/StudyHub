#Faça um programa que faça uma tabuada de um número que usuário escolher.

num = int(input('Me diga um Valor Inteiro qualquer.'))
ate = int(input('Até qual valor deseja saber sua tabuada?'))
mult = 0
for c in range(0,ate):
    mult+=1
    print(f'[{mult}] x [{num}] = {num*mult}')