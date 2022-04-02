#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética. 
#d) Em que posição está o time da Chapecoense.

brasileirao = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')

print(f'Os 5 primeiros times são {brasileirao[0:5]}') #poderia fazer um FOR pra imprimir sem as aspas e etc. Ficaria mais bonito
print(f'Os últimos 4 colocados são: {brasileirao[-4:]}')
print(f'Os times em ordem alfabética são: {sorted(brasileirao)}')
print(f'O time da Chapecoense está na {brasileirao.index("Chapecoense")} posição') #tem que ser aspas duplas pois já estou usando aspas simples no print.