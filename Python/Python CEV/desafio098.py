#Aprimore o Desafio 96
#funcionando com vários jogadores
#incluir um sistema de visualização de detalhes do aproveitamento de cada jogador.

cadastro = []
cont=-1

while True:
    nome = input('Digite o nome do Jogador: ')
    partidas = int(input(f'Quantas partidas {nome} Jogou?'))
    jogador = {'nome': nome, 'gols': [] , 'total':0}
    for i in range(0,partidas):
        gol = int(input(f'Quantos Gols {nome} fez na partida {i}: '))
        jogador['gols'].append(gol)
        jogador['total'] += gol
    cadastro.append(jogador)
    escolha = input('Continuar? [S/N]').upper()
    if escolha == 'N':
        break
print('-='*43)
print(f"{'Cod Nome' : <20}",f"{'Gols' : ^20}",f"{'Total' : >20}")
print('-='*43)

for e in cadastro:
    cont += 1
    nome = e['nome']
    gols = ', '.join(str(gol) for gol in e['gols'])
    print(f"{cont: <3}{nome : <20} {gols : ^20} {e['total']:>20}")


while True:
    opcao = int(input('Escolha um jogador para ter informações detalhadas: '))
    if opcao == 999:
        break
    if opcao < 0 or opcao >= len(cadastro):
        print('Opção inválida. Tente novamente.')
    cont = -1
    print(f'Detalhes do jogador {cadastro[opcao]["nome"]}')
    for e in cadastro[opcao]['gols']:
        cont+=1
        print(f'Na partida {cont} fez {e} Gols.')





