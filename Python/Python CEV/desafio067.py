"""
Crie um programa que leia vários números inteiros
só pare quando o Usuário Digitar 999
Mostre quantos números foram digitados
e a soma entre eles
"""

numero = 0
cont = 0
resultado = 0

print('Digite 999 Para encerrar o programa.')
while True:
    numero = int(input('Digite um número Inteiro: '))
    if numero==999:
        break
    cont+=1
    resultado+=numero
print(f'Você digitou: {cont} Numeros e a Soma entre eles é: {resultado}')
