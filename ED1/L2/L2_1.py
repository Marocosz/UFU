n = int(input("Digite o número que deseje o fatorial: "))

lista = []

def fatorial(num):
    if num < 1:
        return 1
    else:
        return num * fatorial(num-1)


for i in range(n):
    lista.append(i+1)

media = sum(lista)/len(lista)

print(fatorial(n))
print(media)
