#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final mostre a matriz formatada com os números.

numeros = [[],[],[]]

for f in range(1,4):
    for c in range(1,4):
        num= input(f'Digite o valor para F: {f} C: {c}   ')
        numeros[f-1].append(num)

print(f'[ {numeros[0][0]} ] [ {numeros[0][1]} ] [ {numeros[0][2]} ]\n[ {numeros[1][0]} ] [ {numeros[1][1]} ] [ {numeros[1][2]} ]\n[ {numeros[2][0]} ] [ {numeros[2][1]} ] [ {numeros[2][2]} ]')
