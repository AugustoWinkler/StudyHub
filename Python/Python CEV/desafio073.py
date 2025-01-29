"""
Faça um programa que leia um número de 0 a 20 e mostre ele pos extenso
"""


tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um número inteiro: '))
    if not 0 <= num <= 20:
        print('Tente novamente' ,  end=' ')
        continue
    print(f'Você digitou: {tupla[num]}')
    resposta = input('Gostaria de continuar? [S/N]: ').upper()
    if resposta == 'N':
        print('_FIM DO PROGRAMA_')
        break
