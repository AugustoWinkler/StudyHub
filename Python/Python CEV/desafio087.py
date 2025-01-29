#Crie um programa que o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única.
#Que mantenha separado os valores pares e impares, no final mostre os valores pares e impares em ordem crescente.

numeros = [[],[]]


for i in range(0,7):
    num = int(input('Digite um valor: '))
    if num%2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

print(f'Os Valores Pares digitados foram: {sorted(numeros[0])}')
print(f'Os Valores Impares digitados foram: {sorted(numeros[1])}')