#Aprimore o exercicio 89 mostrando no final: a soma dos valores pares.
#a soma dos valores da terceira coluna
#o Maior valor da segunda linha.

#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final mostre a matriz formatada com os números.

numeros = [[],[],[]]
pares = 0

for f in range(1,4):
    for c in range(1,4):
        num= int(input(f'Digite o valor para Linha {f} Coluna {c} : '))
        numeros[f-1].append(num)
        if num%2==0:
            pares+=num
maiorl2 = [numeros[1][0],numeros[1][1],numeros[1][2]]

print(f'[ {numeros[0][0]} ] [ {numeros[0][1]} ] [ {numeros[0][2]} ]\n[ {numeros[1][0]} ] [ {numeros[1][1]} ] [ {numeros[1][2]} ]\n[ {numeros[2][0]} ] [ {numeros[2][1]} ] [ {numeros[2][2]} ]')
print(f'A Soma dos valores pares é: {pares}')
print(f'O Maior valor da Linha 2 é: {max(maiorl2)}')
print(f'A Soma dos números da terceira coluna é: {numeros[0][2]+numeros[1][2]+numeros[2][2]}')
