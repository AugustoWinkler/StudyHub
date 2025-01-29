"""
Crie um programa que leia o ano de nascimento de sete pessoas, e mostre na tela quantas delas não
atingiram a maioridade e quantas já
"""

import datetime
atual = datetime.datetime.now().year
maiores = 0
menores = 0
for c in range (1,8):
    ano = int(input('Qual seu ano de nascimento?'))
    if atual - ano>18:
        maiores+=1
    else:
        menores+=1
if maiores==0:
    print(f'Não tem nínguem maior de idade.\nTodos os {menores} são Menores de idade.')

elif menores==0:
    print(f'Não tem nínguem menor de idade.\nTodos os {maiores} são Maiores de Idade.')
else:
    print(f'Existem {maiores} maiores de idade\nE existem {menores} menores de idade.' )
