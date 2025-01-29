"""
Crie um programa que leia o nome e o preço de vários produtos.
o programa deverá perguntar se o usuário vai continuar, no final mostre:
Qual é o  total gasto da compra:
Quantos produtos custam mais de 1000R$
Qual o nome do produto mais barato.
"""

nome = ''
preco = 0
menor_preco = 9999999999999
barato = ''
escolha = ''
produto_maiorquemil = 0
total = 0

print(f'{"Inicio do Programa.":=^30}')
while True:
    escolha = input('Gostaria de Continuar? [S/N]').upper()
    if escolha=='N':
        break
    elif escolha=='S':
        nome = input('Qual o nome do produto?')
        preco = int(input('O Valor do produto?'))

        total+=preco

        if preco>1000:
            produto_maiorquemil+=1
        if preco<menor_preco:
            menor_preco=preco
            barato=nome

print(f'{"Fim do Programa":=^30}')
print(f'Valor Total da Compra: {total:.2f}\n{produto_maiorquemil} Custam mais de Mil\n{barato} é o Mais Barato.')


