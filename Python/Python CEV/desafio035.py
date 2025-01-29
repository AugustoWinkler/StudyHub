#Objetivo perguntar o valor de salário de um funcionario e calcule o valor do seu aumento
#Valores superiores a 1250.00 o aumento é de 10% para inferiores 15%

x = float(input('Qual o valor de seu salário?:'))

if x>=1250:
    print(f'Seu salário teve um aumento de 10%\nValor Atual: {x:.2f}\nNovo Salário: {x+(x*10/100):.2f}')
else:
    print(f'Seu salário teve um aumento de 15%\nValor Atual: {x:.2f}\nNovo Salário: {x+(x*15/100):.2f}')