#Crie um programa que vai ler vários numeros e guardar em uma lista.
#Depois disso crie duas listas extras que vão conter apenas os valores parese os impares digitados
#Ao final mostre as três listas geradas.
cont = 1
listacompleta = []
listapar = []
listaimpar = []

while True:
    num = int(input(f'Digite o {cont}° Valor: '))
    cont+= 1
    listacompleta.append(num)

    opcao = input('Valor adicionado a lista, Gostaria de continuar? [S/N]').upper()
    if opcao =='N':
        break

for n in listacompleta:
    if n%2==0:
        listapar.append(n)
    if n%2==1:
        listaimpar.append(n)

print('=-'*30)
print(f'Lista Completa: {listacompleta}')
print('=-'*30)
print(f'Lista Par: {listapar}')
print('=-'*30)
print(f'Lista Impar: {listaimpar}')
print('=-'*30)