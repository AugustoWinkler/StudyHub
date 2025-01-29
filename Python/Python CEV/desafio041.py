"""
Crie um programa que leia 2 notas de um aluno
Se a média for abaixo de 5 Aluno Reprovado
Se a média for 5 e 6.9 Aluno está de Recuperação
Se a média for 7 ou superior Aluno está Aprovado
"""
n1 = float(input('Qual sua primeira nota?'))
n2 = float(input('Qual sua segunda nota?'))

media = (n1+n2)/2

if media<5:
    print('Você está reprovado.')
elif media in range (5,7):
    print('Você está de recuperação')
else:
    print('Você está aprovado!')
