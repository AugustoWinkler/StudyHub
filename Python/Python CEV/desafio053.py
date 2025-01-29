num = int(input('Me diga um número Inteiro para saber se ele é primo'))

import math

if num ==2 or num==3:
    print('Ele é Primo.')
elif num%2==0:
    print('Ele Não é Primo.')
else:
    limite= math.floor(math.sqrt(num))
    for c in range(3,limite+1,2):
        if num % c == 0:
            print('Não é Primo')
            break
    else:
        print('é Primo.')