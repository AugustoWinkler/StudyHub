#Crie um programa que leia um nome, ano de nascimento, carteira  de trabalho e cadastre (com idadade)em um dicionario
# Se por acaso a CTPS for diferente de 0 o dicionário recebera também o ano de Contratação e o Salário.
#Calcule e acrescente . além da idade com quantos anos a pessoa vai se aposentar.
import datetime

dic = {'nome':'','idade':'','ctps':'','contratação':'','salário':'','aposentadoria':''}
while True:
    dic ['nome'] = input('Qual seu nome: ')
    anonasci = int(input('Ano de nascimento: '))
    dic ['ctps'] = int(input('Numero Carteira de Trabalho (0 = Não tem) : '))
    if dic['ctps'] == 0:
        break
    dic ['contratação'] = int(input('Ano de Contratação: '))
    dic ['salário'] = int(input('Salário: '))
    break
dic ['idade'] = datetime.date.today().year - anonasci
dic ['aposentadoria'] = dic ['idade'] + 35


for v,k in dic.items():
    if k == 0:
        break
    print(f'O {v} tem valor de {k}')
