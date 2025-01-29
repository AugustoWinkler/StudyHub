"""
Crie um programa que leia a idade e o sexo de várias pessoas
A cada pessoa cadastrada o o programa deverá
A Quantas Pessoas tem mais de 18 anos.
Quantos Homens cadastrados
Quantas Mulheres com menos de 20 anos
"""
idade = 0
sexo = ''
cont_homens = 0
cont_idademaior = 0
cont_mulhermenor20 = 0
escolha = ' '

print(f'{"Cadastre uma Pessoa.":-^30}')
while True:
    escolha = input('Quer continuar? [S/N]').upper()
    if escolha=='N':
        break
    elif escolha=='S':
        idade = int(input('Qual sua idade?'))
        sexo = input('Sexo [M/f]').upper()
        if sexo=='M':
            cont_homens+=1
        if idade>18:
            cont_idademaior+=1
        if sexo=='F' and idade<20:
            cont_mulhermenor20+=1
print(f'{"Final do Programa":-^30}')
print(f'Existem {cont_homens} Homens.\n{cont_idademaior} Maiores de idade.\n{cont_mulhermenor20} Mulheres com menos de 20 anos.')

