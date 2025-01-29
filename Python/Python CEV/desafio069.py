"""
Crie um programa que jogue par ou impar
Se o Jogador perder encerre o programa
e mostre o total de vitórias consecutivas
"""

from random import randint

computador = randint(1,10)
jogador = 0
cont = 0
escolha = ''

print('Vamos Jogar Par ou Impar: ')
while True:
    jogador = int(input('Escolha um número: '))
    escolha = input('Você quer [P/I] ?').upper().strip()[0]
    computador= randint(1,10)
    if escolha=='P':
        if (computador+jogador)%2 ==0:
            print(f'Você venceu! eu escolhi {computador} e você {jogador}, {computador+jogador} é Par')
        else:
            print(f'Você perdeu! eu escolhi {computador} e você {jogador}, {computador+jogador} é Impar')
            break
    elif escolha=='I':
        if (computador + jogador) % 2 == 1:
            print(f'Você venceu! eu escolhi {computador} e você {jogador}, {computador + jogador} é Impar')
        else:
            print(f'Você perdeu! eu escolhi {computador} e você {jogador}, {computador + jogador} é Par')
            break
    cont+=1
print(f'Você venceu {cont} vezes.')
