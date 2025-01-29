"""
Crie um programa que leia 2 valores e mostre um menu na tela
Somar,Multiplicar,maior,novos números, sair do programa
"""


opcao=0

while opcao!=5:
    n1 = int(input('Digite o primeiro valor:'))
    n2 = int(input('Digite o segundo valor:'))
    opcao = int(input('1 [Somar]\n2 [Multiplicar]\n3 [Maior]\n4 [Novos números]\n5 [Sair do Programa]'))
    if opcao==1:
        print(n1 + n2)
    elif opcao==2:
        print(n1 * n2)
    elif opcao==3:
        print(max(n1,n2))
print('Você saiu do programa.')