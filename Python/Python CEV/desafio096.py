#Crie um programa que gerencie o aproveitamento de um jogador de futebol,
#O programa vai ler o nome do jogador e quantas partidas ele jogou, depois ler a quantidade de Gols
# feitos em cada partid. no final tudo isso era guardado em um dicionario incluvindo o total de gols feitos durante o campeonato

jogador = {'nome':'','gols':[], 'total':0}

jogador['nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))

for i in range (0,partidas):
    g = int(input(f'Quantos Gols {jogador["nome"]} fez na partida: {i} ?  '))
    jogador['gols'].append(g)
    jogador['total'] += g
print('-='*20)
print(f'O Jogador {jogador["nome"]} Jogou {partidas} partidas.')
for k in range(0,(len(jogador['gols']))):
     print(f'=> Na Partida {k} teve {jogador["gols"][k]}')
print(f'Totalizando {jogador["total"]} Gols.')
print('-='*20)
