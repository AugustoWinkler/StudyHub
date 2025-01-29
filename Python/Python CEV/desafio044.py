"""
Desenvolva uma lógica que leia o peso e a altura de uma pesso, Calcule seu IMC
e mostre seu Status, de acordo com a tabela a abaixo:
Abaixo de 18.5: Abaixo do peso
Entre 18.5 e 25: Peso Ideal
25 até 30: Sobre peso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida
"""

peso = float(input('Qual seu peso?'))
altura = float(input('Qual sua altura?'))

imc = peso/(altura*altura)

if imc<18.5:
    print('Você está abaixo do peso.')
elif imc<25:
    print('Você está no peso ideal.')
elif imc<30:
    print('Você está com Sobre Peso.')
elif imc<40:
    print('Você está Obeso.')
else:
    print('Você está em estado de Obesidade mórbida.')
print(f'Seu IMC é: {imc:.2f}.')