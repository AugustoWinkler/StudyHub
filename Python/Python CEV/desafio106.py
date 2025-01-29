#Crie uma função chamada ficha(), que receba dois parametros opcionais o nome de um jogador e quantos gols ele marcou
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamenta

jogador = input('Nome do Jogador: ')
gols = input(f'Quantidade de Gols de {jogador} : ')

def ficha(nome = '<desconhecido>' , gol = '0'):
    if nome.strip() == '':
        nome = '<desconhecido>'
    if gols.isnumeric() == False:
        gol = 0
    print(f'O Jogador {nome}, Fez {gol} no Campeonato.')

ficha(jogador,gols)
