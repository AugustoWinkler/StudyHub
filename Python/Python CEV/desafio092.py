#Crie um programa que leia o nome e duas notas de alunos e guarde em uma lista composta, no final mostre
#um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

data = []

while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1:'))
    n2 = float(input('Nota 2:'))
    aluno = [nome,((n1+n2)/2)]
    notas = [n1,n2]
    aluno.append(notas)
    data.append(aluno)
    opcao = input('Continuar? [S/N]').upper()
    if opcao == 'N':
        break

print('-='*20)
for e in range(0, len(data)):
    print(f'Aluno {e+1}: {data[e][0]} Média: {data[e][1]}')
print('-='*20)

while True:
    escolha = int(input('Escolha um aluno para ver as Notas! 999 Termina o Programa.'))
    if escolha == 999:
        break
    else:
        escolha-=1
        print(f'Aluno: {data[escolha][0]} Notas: {data[escolha][2]} Media: {data[escolha][1]}')
        print('-=' * 20)

print('Fim do Programa.')
print('-='*20)