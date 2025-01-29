#Faça um Programa que leia o Salário de um Funcionario e Mostre seu novo salário com 15% de aumento
nome = input('Qual seu nome?')
x = float(input('Qual seu salário?'))

a = 15*x/100

print('Parabéns {} , seu antigo salário foi de {:.2f} R$ para {:.2f} R$ (15% de aumento)'.format(nome, x , x+a))