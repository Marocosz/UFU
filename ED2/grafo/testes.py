lista = [1, 2, 3, 4]
aux = lista
lista =  aux
print(lista)
print(aux)

aux.remove(lista[0])
print(lista)
print(aux)