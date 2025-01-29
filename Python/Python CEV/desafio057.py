#Desenvolva um programa que leia o nome,idade e sexo de 4 pessoas, no final do programa mostre:
#A Média de idade do grupo, Qual o nome do homem mais velho e quantas mulheres tem menos de 20 anos.
mediaidade = 0
maioridadehomem=0
somaidade=0
nomevelho=''
totmulher20=0

for p in range(1,5):
    print(f'----- {p}° PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]')).strip()
    somaidade += idade
    if p==1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade>maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade<20:
        totmulher20+=1



mediaidade = somaidade/4
print(f'A Média de idade do grupo é: {mediaidade} anos')
print(f'O Homem mais velho tem {maioridadehomem} Anos e se chama: {nomevelho}.')
print(f'Ao todo são {totmulher20} Mulheres menor de 20 Anos.')