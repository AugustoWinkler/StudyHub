#Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações
# Quantidade de notas, Maior Nota, A Menor Nota a Média da turma a Situação Opicional

alunos = dict()
def notas(*num, sit=True):
    """

    :param num: Recebe quantidade de notas (Qualquer quantidade)
    :param sit: (False por Padrão) se True mostra a situação entre (Boa,Razoavel e Ruim) baseada na média
    :return: quantidade de num, maior num,menor num, média de num
    """
    alunos['quantidade'] = len(num)
    alunos['maior'] = max(*num)
    alunos['menor'] = min(*num)
    alunos['média'] = sum(num)/alunos['quantidade']
    if sit==True:
        if alunos['média'] <=5:
            alunos['situação'] = 'Ruim'
        elif alunos['média']>=7:
            alunos['situação'] = 'Boa'
        else:
            alunos['situação'] = 'Razoavel'


print(notas(2,7.5,4,9,5) , alunos)
