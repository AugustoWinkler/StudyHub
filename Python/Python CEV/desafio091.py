#Crie um programa que gere palpites para MegaSena o programa vai perguntar quantos jogos serão geradose vai sortear
#6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
palpite= []
jogos = []
a = randint(1,60)

cont = int(input('Quantos Jogos da Mega Sena gostaria de Gerar?'))
print('-='*2,f'Gerando {cont} Jogos da Mega Sena.' ,'-='*2)

for jogo in range(0,cont):
    for p in range(0,6):
        while a in palpite:
            a = randint(1, 60)
        palpite.append(a)
    jogos.append(palpite[:])
    palpite.clear()

for c in range(0,len(jogos)):
    print(f'Jogo [{c+1}] :  {sorted(jogos[c])}')
    sleep(0.4)

print('-='*4,'< Boa Sorte! >' ,'-='*4)



