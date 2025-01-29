#Utilizando modulos crie um modulo moeda.py  que tenha funções incorporadas aumentar(),Dimunuir(),dobro(),metade()

def aumentar(n,x,f=False):
    if f==True:
        return f'R$ {n*x/100+n:.2f} '
    return n * x / 100 + n


def diminuir(n,y,f=False):
    if f==True:
        return f'R$ {abs(n * y / 100 - n):.2f}'
    return abs(n * y / 100 - n)


def dobro(n,f=False):
    if f==True:
        return f'R$ {n*2:.2f}'
    return n*2


def metade(n, f=False):
    if f==True:
        return f'R$ {n/2:.2f}'
    return n/2

def moeda(n):
    return f'R$ {n:.2f}'

def tittle(txt):
    tam = len(txt)
    return f"~" * (tam + 10) + "\n" + f"     {txt}\n" + f"~" * (tam + 10)


def resumo(n,x,y):
    print(tittle('RESUMO DO VALOR.'))
    print(f'Preço Analisado: {moeda(n):>14}')
    print(f'Dobro do Preço: {moeda(n*2):>16}')
    print(f'Metade do Preço: {moeda(n/2):>14}')
    print(f'{x}% de Aumento: {moeda(n*x/100+n):>15}')
    print(f'{y}% de Redução: {moeda(abs(n*y/100-n)):>15}')

