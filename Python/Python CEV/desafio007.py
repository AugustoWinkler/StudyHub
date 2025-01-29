#Objetivo Criar um Programa que leia 2 Notas de um Aluno e calcule sua Média
n = input('Nome do Aluno:')
n1 = int(input('Digite a nota da Primeira prova:'))
n2 = int(input('Digite a nota da Segunda prova:'))

print('Parabéns {:=^15} a sua nota média é: {}'.format( n , (n1 + n2) /2))
