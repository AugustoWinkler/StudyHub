#Crie uma função que contenha área e Largura de um terreno e mostre a area


def terreno(a,b):
    area = a*b
    print(f'Largura {a} X Comprimento {b} Igual Área {area:.0f} m2')


a = float(input('Digite a largura do terreno: '))
b = float(input('Digite o comprimento do terreno: '))
terreno(a, b)