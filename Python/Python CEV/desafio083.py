#Objetivo crie um programa que vai ler vários números e colocar em uma lista.
#Depois mostre quantos números foram digitados, A Lista de Valores ordenada de forma decrescente
#e se o valor 5 está na lista.
cont = 1
lista = []
while True:
    num = int(input(f'Digite o valor: {cont}° '))
    cont+=1
    lista.append(num)
    opcao = input('Gostaria de continuar? [S/N}').upper()
    if opcao=='N':
        break

lista.sort(reverse=True)
print('-='*25)
print(f'Foram Digitados {len(lista)} Numeros.')
print('-='*25)
print(f'A Lista em forma Decrescente fica desta forma. {lista}')
print('-='*25)
if 5 in lista:
    print(f'Você digitou o valor 5 e ele se encontra na Posição: {lista.index(5)+1}')
else:
    print('a lista não possui o valor 5 .')