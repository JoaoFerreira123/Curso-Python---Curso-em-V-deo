#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import Moeda107


num = int(input('Digite um número: '))
print(Moeda107.aumentar(num, 2))
print(Moeda107.diminuir(num, 2))
print(Moeda107.dobro(num))
print(Moeda107.metade(num))