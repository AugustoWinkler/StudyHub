#Crie um programa que pergunte a distancia de uma viagem em KM, calcule o preço da passagem
#0,50 Centavos por KM para viagens em até 200km/h e 0,45 Centavos para viagens mais longas


x=float(input('Quantos Km é seu Destino?'))

if x<=200:
    print(f'Cada KM é cobrado 0,50 Centavos\nO Valor da viagem será de: {x*0.50:.2f}')
else:
    print(f'Para viagens acima de 200KM o Valor cobrado é de 0,45 Centavos\nO Valor da viagem será de:{x*0.45:.2f}')