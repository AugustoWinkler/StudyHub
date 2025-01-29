#Crie um programa onde o usuário pode digitar vários valores numéricos
#Cadastre-os em uma lista, Caso o valor já esteja lá, ele não será adicionado.
#No final serão impressos todos os valores únicos em ordem crescente.
lista= []

while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Adicionado com Sucesso...')
    else:
        print('Numero duplicado, não vou adicionar...')
    opcao = input('Gostaria de Continuar? [S/N]').upper()
    if opcao == 'N':
        break

print(f'Você digitou os valores {sorted(lista)}')