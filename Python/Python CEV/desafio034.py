#faça um programa que leia 3 números e Mostre qual o maior e qual o menor:

n1 = int(input('Qual o primeiro número?'))
n2 = int(input('Qual o segundo número?'))
n3 = int(input('Qual o terceiro número?:'))

menor_valor = min(n1,n2,n3)
maior_valor= max(n1,n2,n3)

print(f'O Menor valor é: {menor_valor}\nO Maior valor é: {maior_valor}')