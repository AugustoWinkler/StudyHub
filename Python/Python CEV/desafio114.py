#Reescreva a função leiaint() agora com a possibilidade da digitação de um número de tipo inválido.
#Aproveite e crie uma função leiafloat() com a mesma funcionalidade.

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print('Usuario preferiu não informar um valor.')
            return 0
        except(ValueError, TypeError):
            print('Erro digite um valor válido.')
            continue
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except KeyboardInterrupt:
            print('Usuario preferiu não informar um valor.')
            return 0
        except(ValueError, TypeError):
            print('Erro digite um valor válido.')
            continue
        else:
            return n

num1 = leiaint('Digite um Valor Inteiro: ')
num2 = leiafloat('Digite um Valor Real? ')
print(f'O Valor Inteiro digitado foi {num1} e o Valor Real digitado foi {num2}')

