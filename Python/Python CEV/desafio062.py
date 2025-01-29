"""
Refaça o Desafio 52, Lendo o primeiro termo e a razão de uma PA  e mostre os 10 primeiros termos da progressão
usando a estrutura While
"""
termo = int(input('Qual o Termo da PA?'))
razao = int(input('Qual a Razão da PA?'))
contador=0

while contador!=10:
    print(termo, end=' ')
    contador+=1
    termo+=razao
