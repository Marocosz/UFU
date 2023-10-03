n = int(input('Digite quantos termos voce quer: '))
r = int(input('Digite a razão da PG: '))
t1 = int(input('Digite o primeiro algarismo da PG: '))


def pg(n):
    if n == 1:
        return t1
    else:
        return r * pg(n-1)
    

lista = []
    
for x in range(1, n + 1):
    valor = pg(x)
    lista.append(valor)


print(lista)