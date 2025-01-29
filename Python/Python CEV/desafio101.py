#Faça uma função chamada contador que tenha 3 parametros: inicio fim e passo e realize 3 contagens
#de 1 até 10 Pulando de 1 em 1
#de 10 até 0 pulando de 2 em 2
#uma contagem personalizada
from time import sleep

def contador(a,b,c):
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if c==0:
        c = 1
    if a>b:
        c = -abs(c)
        b = b-1
    else:
        b+=1
    for i in range (a,b,c):
        print(i , end=' ' , flush=True)
        sleep(0.2)
    print('')
def lin():
    print('-='*20)

lin()
contador(1,10,1)
lin()
contador(10,0,2)
lin()
print('Agora faça você sua contagem!')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
lin()
contador(a,b,c)
lin()


