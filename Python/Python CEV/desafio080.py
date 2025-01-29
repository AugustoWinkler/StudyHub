#Objetivo Faça um programa que leia 5 valores e guarde em uma lista
#no final mostre qual foi o maior e menor valor digitado
#e suas respectivas posições digitadas

lista = []
maior = float('-inf')
menor = float('inf')

# Recebe os valores e guarda na lista.
for cont in range(0, 5):
    valor = int(input(f'Digite um valor para posição {cont+1}: '))
    lista.append(valor)

# Encontra o maior e o menor valor.
for pos, valor in enumerate(lista):
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

posmaior = [pos +1 for pos, valor in enumerate(lista) if valor == maior]
posmenor = [pos  +1 for pos, valor in enumerate(lista) if valor == menor]

print('-=' * 20)
print(f'Os números digitados foram: {lista}')
print('-=' * 20)

print(f'O maior valor foi: {maior} encontrado nas posições {posmaior}')
print('-=' * 20)
print(f'O menor valor foi: {menor} encontrado nas posições {posmenor}')
print('-=' * 20)





