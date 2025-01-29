#Escreva um programa que leia a velocidade de um carro, se ele estiver a cima de 80km/h ele será multado
#O Valor da multa será de 7R$ por KM a cima da velocidade

x = int(input('Qual a velocidade do carro?:'))

if x>=80:
    print(f"""Você foi multado por excesso de velocidade! 
    o máximo da via é 80km/h e você estava á {x}
    Receberá uma multa de {(x-80)*7:.2f}""")
else:
    print('Você está na velocidade permitida da via\ncontinue seu caminho com atenção e Boa sorte!')