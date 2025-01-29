"""
Crie um programa que tenha uma TUPLA única com nomes de produtos e seus preços respectivos na sequencia,
No Final mostre uma Lista de Preços
Organizando os Dados em forma Tabular
"""

produtos = ('Lápis' , 1.75 , 'Borracha' , 2.0 , 'Caderno' , 15.90 , 'Estojo' , 25.00 , 'Transferidor' , 4.20 , 'Compasso' , 9.99 , 'Mochila' , 120.32 , 'Canetas' , 22.30 , 'Livro' , 34.90)


print('-' * 52)
print(' ' * 17 + 'LISTAGEM DE PREÇOS')
print('-' * 52)
for c in range(0, len(produtos), 2):
    print(produtos[c], end='')
    print('.' * (42 - len(produtos[c])), end='')
    print(f'R$ {produtos[c+1]:7.2f}')
print('-' * 52)