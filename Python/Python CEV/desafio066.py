
numero = 1
contador = 0
acomulador = 0
maior = 0
menor = 99999999999
opcao = 'S'
while opcao=='S':
    opcao = input('Continuar? [S/N]').upper()
    if opcao=='S':
        numero = int(input('Digite um valor inteiro: '))
        contador+=1
        acomulador += numero
        if numero>maior:
            maior = numero
        elif numero<menor:
         menor = numero


print(f'Menor {menor} , Maior {maior} , Contagem {contador} , média {acomulador/contador} , soma {acomulador}')


