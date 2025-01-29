#Objetivo crie um programa que leia o nome inteiro de uma pessoa e mostre
#O Nome com todas letras maiusculas
#O Nome com todas letras minusculas
#Quantas letras ao total (sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = input('Qual seu nome completo?')

d1 = nome.upper()
d2 = nome.lower()
d3 = len(nome.strip().replace(' ',''))
d4 = len(nome.split()[0])

print(f"""O Seu nome com Letras Maiusculas: {d1}
O Seu nome com letras minusculas: {d2}
Ele tem ao todo: {d3} Caracteres
Seu primeiro nome possui {d4} letras""")