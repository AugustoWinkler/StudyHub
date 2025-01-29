"""
Objetivo: Faça um programa que calcule o Empréstimo para comprar uma casa:
Perguntar o valor da casa, o salário e em quantos anos pretende pagar
Calcule o valor da prestação mensal e não pode exceder 30% do Salário caso contrário o Empréstimo Sera Negado.
"""

casa =float(input('Qual o valor do imóvel?:'))
salario =float(input('Qual seu salário Mensal?:'))
ano =float(input('Em Quantos anos pretende financiar o imóvel?:'))

parcela = (casa/ano)/12 #Valor das Parcelas em Meses
limite = salario*30/100

if parcela>=limite:
    print(f'Seu Empréstimo foi negado, as parcelas são maiores que 30% do seu Salário.\nValor Parcela: {parcela:.2f}')
else:
    print(f'Seu Empréstimo foi aprovado, o valor das parcelas é: {parcela:.2f} R$, durante {ano:.0f} anos.')