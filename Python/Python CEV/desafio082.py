#Crie um programa que o usuário digite 5 números e cadastre em uma lista.
#já na posição correta de inscrição (sem usar o sort) no final mostre a lista ordenada na tela
lista = []

for _ in range(5):
    num = int(input('Digite um valor: '))
    if len(lista) == 0 or num > lista[-1]:
        print('Valor adicionado ao fim da lista.')
        lista.append(num)
    else:
        for i in range(len(lista)):
            if num <= lista[i]:
                lista.insert(i, num)
                print(f'Valor adicionado da posição: {i+1}')
                break

print(lista)
