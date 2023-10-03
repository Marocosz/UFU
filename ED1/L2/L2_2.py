n = int(input("Digite o número que deseje o fatorial: "))

lista = []

def fatorial(num):
    if num < 1:
        return 1
    else:
        return num * fatorial(num-1)


def media(lista):
    soma = 0
    for x in lista:
        soma = soma + x

    return soma/len(lista)


for i in range(n):
    lista.append(i+1)


print(media(lista))
print(fatorial(n))
