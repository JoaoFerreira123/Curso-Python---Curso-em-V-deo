#Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
from Moeda109 import metade, dobro, aumentar, diminuir, moeda

num = float(input('Digitte um valor: '))
print(f'A metade de {moeda(num)} é {metade(num, True)}')