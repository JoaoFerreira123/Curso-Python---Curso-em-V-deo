#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = input('Digite o nome da cidade: ').strip() #já coloca o strip pra remover os espaços em branco
cidade = cidade.upper().split() #coloca tudo em maiusculo e divide 
print('SANTO' in cidade[0])
