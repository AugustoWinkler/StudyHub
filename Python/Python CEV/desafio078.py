"""
Crie um programa que uma tupla com várias palavras
(não usar acentos)
Depois disso, mostrar na tela cada palavra e suas vogais.
"""

lista = ('aprender' , 'programar' , 'linguagem' , 'python' , 'curso' , 'gratis' ,
         'estudar' , 'praticar' , 'trabalhar' , 'mercado' , 'programador' ,  'futuro')
vogais = []
for palavra in lista:
    vogais = []
    for letra in palavra:
        if letra.lower() in 'aeiou':
            vogais.append(letra)
    print(f'\033[36mVogais na palavra \033[35m{palavra.upper()}\033[36m Temos:\033[33m' , ' '.join(vogais))
