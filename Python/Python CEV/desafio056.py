#Crie um programa que leia o peso de cinco pessoas, no final mostre qual foi o maior e o menor peso lidos.
peso1 = int(input(f'Qual o peso da {1}° Pessoa?'))
maior = peso1
menor = peso1
for c in range (2,6):
    peso = int(input(f'Qual o peso da {c}° Pessoa?'))
    if peso>maior:
        maior=peso
    elif peso<menor:
        menor=peso
print(f'O maior Peso é: {maior}\nO menor Peso é: {menor}')