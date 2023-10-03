n = int(input('Digite quantos termos terá a PA: '))
r = float(input('Digite a razão dessa PA: '))
t1 = float(input('Digite o primeiro termo dessa PA: '))

soma = 0

lista = []
lista.append(t1)

for x in range(n - 1):
    lista.append(lista[x] + r)

for i in lista:
    soma = soma + i

print(lista)
print(soma)