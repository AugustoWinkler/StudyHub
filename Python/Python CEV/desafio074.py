"""
Crie uma Tupla que contenha os 20 Primeiros Colocados na Tabela do Campeonato Brasileiro de Futebol
Depois mostre os 5 Primeiros, Os Ultimos 4 Colocados, Uma Lista com os Times em ordem Alfabetica
e em que posição está o Time da Corinthians.
"""

times = ('Botafogo', 'Palmeiras', 'Fluminense', 'Cruzeiro', 'Athletico PR', 'Atlético-MG', 'Santos',
         'Fortaleza','Flamengo', 'São Paulo', 'Grêmio', 'Internacional', 'Red Bull Bragantino', 'Bahia',
         'Goiás', 'Vasco da Gama','Corinthians', 'Cuiabá-MT', 'Coritiba', 'América-MG')
print(times)
print(sorted(times))
print(times[0:5])
print(times[-5:-1])
print(times.index('Corinthians') + 1)