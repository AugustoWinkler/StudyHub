"""
Elabore um programa que calcule o valor a ser pago por um produto.
considerando seu preço normal e condição de pagamento
a vista/dinheiro/cheque : 10% De Desconto
a vista no cartão: 5% De Desconto
em até 2x no cartão: preço normal.
3x ou mais: 30% de Juros
"""

pagamento = int(input('Qual a forma de pagamento?:\n1 = Dinheiro/Cheque\n2 = Cartão a Vista\n3 = 2 Parcelas Cartão\n4 = 3 Parcelas ou mais Cartão.'))

produto = 50.00

if pagamento==1:
    print(f'Valor Produto: {produto}R$, Porem com sua forma de pagamento, você recebe desconto de 10% Totalizando: {produto-(produto*10/100):.2f}')
elif pagamento==2:
    print(f'Valor Produto: {produto}R$, Porem com sua forma de pagamento, você recebe desconto de 5% Totalizando: {produto-(produto*5/100):.2f}')
elif pagamento==3:
    print(f'Você pagara {produto}R$')
elif pagamento==4:
    print(f'Valor Produto: {produto}R$, Porem Parcelas a cima de 3x tem Juros de 30% Totalizando{produto+(produto*30/100)}')
else:
    print('Você colocou uma opção Invalida.')