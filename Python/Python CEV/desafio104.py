#Crie um programa com função voto
#parametro ano de nascimento
#Retornar um valor literal indicando se voto Negado,Opicional ou Obrigatório nas eleições


def voto(x):
    from datetime import date
    atual = date.today().year
    idade = atual-x

    if idade<16:
       return f'Com {idade} Anos: NÃO VOTA.'
    elif idade<18 and idade>=16 or idade>65:
        return f'Com {idade} Anos: VOTO OPICIONAL.'
    else:
        return f'Com {idade} Anos: VOTO OBRIGATÓRIO.'


ano = int(input('Ano de Nascimento: '))
print(voto(ano))
