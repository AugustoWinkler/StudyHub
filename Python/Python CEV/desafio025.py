#Objetivo faça um programa que leia o nome de uma cidade e Diga se ela começa com Santo ou não

x = input('Qual o nome da cidade?:')

cidade = x.strip().upper().split()
primeiro = cidade[0]
nova = 'SANTO' in primeiro

if nova==False:
    print(f'Sua cidade não começa com Santo, ela começa com {primeiro.title()}')
else:
    print('Sua Cidade começa com Santo')