#Crie uma função que calcule um fatorial com 2 Parâmetros o Número Fatorial e a Opção 'Show'
#Se Show ativo mostre o processo de calculo do Fatorial

def calcfatorial(x=0, show=False):
    """
    :param x: Pega um Valor para Fatorizar
    :param show: False por Padrão, Caso True mostra o processo do Calculo Fatorial
    :return: Valor Fatorial do Param X.
    """
    fatorial = 1
    for c in range(x,0,-1):
        if show:
            print(c, end='')
            if c>1:
                print(' x ', end='')
            else:
                print(' = ' ,  end='')
        fatorial*=c
    return fatorial


print(calcfatorial(5, show=True))

#help(calcfatorial)