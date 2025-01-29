#Crie um programa que leia nome,sexo e idade de várias pessoas.
#Guarde em um Dicionario e todos dicionarios em uma lista. no final, mostre:
#Quantas pessoas foram cadastradas
#a média de idade do grupo
#Uma lista com todas as mulheres
#Uma lista com todos com a idade acima da média.

cadastro = []
media =0
mulheres = []
acimedia = []

while True:
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    pessoa = {'nome':nome ,  'idade':idade , 'sexo': sexo}
    cadastro.append(pessoa.copy())
    escolha = input('Continuar [S/N]: ').upper()
    if escolha == 'N':
        break
for e in cadastro:
    media += e['idade']
    if e['sexo'] == 'F':
        mulheres.append(e['nome'])

for e in cadastro:
    if e['idade']>media//len(cadastro):
        acimedia.append(e['nome'])

print(f'Média de idade {media//len(cadastro)}')
print(f'Quantidade de pessoas cadastradas: {len(cadastro)}')
print(f'Mulheres cadastradas {mulheres}')
print(f'Pessoas a cima da idade média: {acimedia}')

