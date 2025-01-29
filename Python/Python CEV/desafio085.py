#Crie um programa que leia uma expressão com parenteses e diga se ela é válida pela quantidade de parenteses:
parentesesfechado = []
parentesesaberto = []
exp = input('Digite a expressão: ')

for i in exp:
    if i=='(':
        parentesesaberto.append(i)
    elif i==')':
        parentesesfechado.append(i)

if len(parentesesaberto)/len(parentesesfechado)==1:
    print('Está expressão é valida.')
else:
    print('Está expressão é inválida.')