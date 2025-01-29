"""
A Confederação Nacional de Natação, precisa de um programa que leia o ano de nascimento de um Atleta
e Mostre sua categoria de acordo com a idade:
até 9 Anos: Mirim
até 14 Anos: Infantil
até 19 Anos: Junior
até 20 Anos: Sênior
Acima: Master
"""
import datetime
ano = int(input('Em qual ano foi nascido o atleta?:'))

idade = datetime.datetime.now().year-ano

if idade<9:
    print('Você é um Atleta Mirim!')
elif idade in range (9,14):
    print('Você é um Atleta Infantil!')
elif idade in range(14,19):
    print('Você é um Atleta Junior!')
elif idade in range (19,20):
    print('Você é um Atleta Sênior')
else:
    print('Você é um Atleta Master!')