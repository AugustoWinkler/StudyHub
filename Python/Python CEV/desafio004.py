#Objetivo Fazer um programa que leia um input e mostre seu Tipo Primitivo e suas caracteristicas
x = input('Digite alguma coisa:')

print('Ele é Alpha:' , x.isalpha())
print('Ele é Numeric:' , x.isnumeric())
print('Ele é Alphanumérico:' , x.isalnum())
print('Ele é Minusculo:' , x.islower())
print('Ele é Maiusculo:' , x.isupper())
print('Ele é imprimivel:' , x.isprintable())
print('Seu tipo Primitivo é: ', type(x))
