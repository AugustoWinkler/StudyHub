#Objetivo faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra 'A'
#Em que Posição ela aparece pela primeira  vez
#Em que Posição ela aparece pela última vez

x = input('Qual sua Frase?:')

contador = x.upper().count('A')+1
primeira = x.upper().find('A')+1
ultima = x.upper().rfind('A')

print(f"""Sua Frase possui {contador} letras 'A' 
a Primeira letra 'A' aparece {primeira} posição
e a Ultima letra 'A' aparece {ultima} posição""")
