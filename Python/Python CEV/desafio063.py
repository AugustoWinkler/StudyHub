"""
Refaça o Desafio 52, Lendo o primeiro termo e a razão de uma PA  e mostre os 10 primeiros termos da progressão
usando a estrutura While
Porem agora quando terminar os 10 Termos, pergunte se a pessoa quer mais termos se sim quantos
"""
termo = int(input('Qual o Termo da PA?'))
razao = int(input('Qual a Razaão da PA?'))
contador = 0
opcao = 3
while contador<10:
    print(termo, end=' ')
    contador += 1
    termo += razao
while opcao!=0:
    opcao = int(input('Mais termos?\n0 [NÃO]\n1 [SIM]'))
    if opcao==1:
        quantidade = int(input('Quantos termos?'))
        contador=0
        while contador<quantidade:
            print(termo, end=' ')
            contador+=1
            termo += razao
    else:
        print('Obrigado!')
print('FIM')