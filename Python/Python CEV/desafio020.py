#Faça um programa que leia um angulo qualquer e mostre o Seno, Cosceno e Tangente dele

import math

x = int(input('Me diga o valor do Angulo:'))

r = math.radians(x)
s = math.sin(r)
c = math.cos(r)
t = math.tan(r)

print(f'O Seno é: {s:.4f} O Cosseno é: {c:.4f} e a Tangente é: {t:.4f}')