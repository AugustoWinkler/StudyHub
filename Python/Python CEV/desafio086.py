#Faça um programa que leia vários nomes e pesos de pessoas diferentes
#no final mostre as pessoas mais pesadas e mais leves e quantas pessoas foram cadastradas.

cadastro = []
lista = []
maiorp= 0
menorp= float('inf')
maiores = []
menores = []

while True:
    pessoa= input('Nome: ')
    peso= int(input('Peso: '))
    cadastro.append(pessoa)
    cadastro.append(peso)
    lista.append(cadastro[:])
    cadastro.clear()
    opcao = input('Gostaria de Continuar? [S/N]').upper()
    if opcao =='N':
        break

for p in lista:
    if p[1]> maiorp:
        maiorp=p[1]
        maiores.clear()
        maiores.append(p[0])
    elif p[1]==maiorp:
        maiores.append(p[0])
    if p[1]<menorp:
        menorp=p[1]
        menores.clear()
        menores.append(p[0])
    elif p[1]==menorp:
        menores.append(p[0])

print('-='*25)
print(f'Você cadastrou {len(lista)} Pessoas.')
print('-='*25)
print(f'As pessoas mais pesadas pesam: {maiorp} e são: {maiores}')
print('-='*25)
print(f'As pessoas mais leves pesam: {menorp} e são: {menores}')
print('-='*25)
