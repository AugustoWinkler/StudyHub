#Função escreva recebe um texto qualquer como parametro e mostre na tela com um tamanho adaptavel

def escreva(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
escreva('Desafio Concluido com Sucesso!')