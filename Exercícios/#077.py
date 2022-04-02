#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('abacaxi', 'banana', 'melancia', 'manga')
vogais = ('a', 'e', 'i', 'o', 'u')
for i in palavras:
    print(f'\nNa palavra {i} temos:', end = '')
    for j in i: 
        if j in 'aeiou':
            print(j, end = ' ')

#o primeiro FOR ele pega palavra a palavra. Ou seja, o i é cada palavra. 
#mas cada palavra também tem seus índices, o j percorre cada palavra, ou seja, j percorre i (for j in i)
#dai o if pra verificar se tiver "aeiou" em j (letra). ou seja, se a letra for uma vogal, ele mostra a letra (j)