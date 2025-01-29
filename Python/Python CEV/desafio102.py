#Faça uma função maior() que receba vários parametros com valores inteiros, ela deve analisar e retornar o maior deles
from time import sleep

def maior(*num):
    tam = len(num)
    print('-='*30)
    print('Analisando os Valores passados...')
    for e in num:
        print(e , end=' ')
        sleep(0.1)
    print(f'Foram informados {tam} ao todo.')
    print(f'O Maior valor informado foi: {max(num)}')
    print('-='*30)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(0)