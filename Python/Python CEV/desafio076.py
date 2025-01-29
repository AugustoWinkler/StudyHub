"""
Crie um Programa que leia 4 Valores pelo Teclado e guarde os em uma tupla, no final Mostre
Quantas vezes apareceu o valor 9
em que posição foi digitado o primeiro valor 3
quais foram os números pares
"""

numero = (int(input('Digite um Valor: ')),int(input('Digite outro Valor: ')),
          int(input('Digite mais um Valor: ')),int(input('Digite o ultimo Valor: ')))
print('Valores Digitados:' ,  numero )
if 9 in numero:
    print(f'O Valor nove apareceu {numero.count(9)} vez(es)')
else:
    print(f'Não tem 9 Nos valores digitados.')
if 3 in numero:
    print(f'O Valor 3 foi digitado na posição {numero.index(3)+1}')
else:
    print(f'Não tem o Valor 3 nos Números Digitados.')

for i in numero:
    if i%2==0:
        print(f'O Número: {i} é par.' , end=' ')


print('\n__FIM__')




