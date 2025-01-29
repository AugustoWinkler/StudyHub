#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos seus digitos separados

x = int(input('Me diga um valor inteiro de 0 a 9999: '))

unidade = x % 10
x = (x - unidade)/10

dezena = x % 10
x =  (x - dezena)/10

centena = x % 10
x = (x - centena)/10

milhar = x % 10

print(f"""Unidade(s): {unidade}
Dezena(s): {dezena:.0f}
Centena(s): {centena:.0f}
Milhar(es): {milhar:.0f}""")