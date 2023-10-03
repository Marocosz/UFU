n = int(input('Digite quantos termos terá a PG: '))
r = float(input('Digite a razão dessa PG: '))
t1 = float(input('Digite o primeiro termo dessa PG: '))

produto = 1

lista = []
lista.append(t1)

for x in range(n-1):
    lista.append(lista[x]*r)

for i in lista:
    produto = produto * i

print(lista)
print(produto)