#Crie um programa que leia uma frase qualquer e diga se ela é um Palindromo

entrada = input('Digite uma frase: ')

frase = entrada.upper().strip().replace(' ','')
reverse = frase[::-1]

if frase == reverse:
    print('Sua frase é um Palindromo')
else:
    print('Ela não é um Palindromo')