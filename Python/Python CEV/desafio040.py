"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
-Se ele ainda vai se alistar
- Se estiver na hora de alistar
- Se já passou do tempo de alistamento
O Programa também deve mostrar o tempo que falta ou que passou
"""

ano = int(input('Qual seu ano de nascimento?'))

passaram = 2023-ano-18
idade = 2023-ano
faltam = 18 - idade

if idade==18:
    print('Está na hora de se alistar.')
elif idade>18:
    print(f'Já passaram {passaram} Anos de seu Alistamento.')
else:
    print(f'Você tem apenas {idade}, Faltam {faltam} Anos para se Alistar.')