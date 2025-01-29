"""
Faça um programa que leia o Sexo de uma pessoa, mas só aceite se for "M" ou "F"
Caso esteja errado peça a digitação novamente  até ter um valor correto
"""


sexo = input('Sexo [M/F] : ').upper().strip()
while sexo not in 'MF':
    sexo = input('Dados inváilidos, Por favor informe seu Sexo : ').upper()

print(f'Sexo: {sexo}  registrado com sucesso. ')
