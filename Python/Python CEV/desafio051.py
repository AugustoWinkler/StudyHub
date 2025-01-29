#Faça um programa que leia 6 números inteiros e mostre a soma daqueles que forem Par
resultado=0
for c in range(1,7):
    soma=int(input(f'Digite {c}° valor'))
    if soma%2==0:
        resultado+=soma
print(f'A Soma de todos os valores pares é: {resultado}')