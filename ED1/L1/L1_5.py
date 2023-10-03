n = int(input('Digite quantos termos terá a PA: '))
r = float(input('Digite a razão dessa PA: '))
t1 = float(input('Digite o primeiro termo dessa PA: '))
max = float(input('Digite o valor max do termo que vamos somar: '))

soma = 0

lista = []
lista.append(t1)

lista_par = []

for x in range(n - 1):
    lista.append(lista[x] + r)

for i in lista:
    if i % 2 == 0:
        lista_par.append(i)
        if i < max:
            soma = soma + i

print(lista)
print(lista_par)
print(soma)