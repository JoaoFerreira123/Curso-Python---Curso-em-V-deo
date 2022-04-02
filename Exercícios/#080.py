#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

num = []
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    #ou adiciona na 1º posição, ou na ultima, ou no meio. Tem essas 3 possibilidades
    if i == 0 or  n > num[len(num)-1]: #se o valor digitado for maior do que o ultimo valor OU igual a zero
        num.append(n)
        #adiciona ao final da lista
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                #adiciona na posição do meio
                break
            pos +=1
print(num)