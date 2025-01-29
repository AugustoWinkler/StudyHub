aluno = {'Nome':'','Média':'','Situação':''}

aluno ['Nome'] = input('Nome do Aluno: ')
aluno ['Média'] = float(input('Media do Aluno: '))
if aluno['Média']>5:
    aluno ['Situação'] = 'Aprovado:'
else:
    aluno ['Situação'] = 'Reprovado: '

for v,i in aluno.items():
    print(f'{v} = {i}.')




