

def criarlista(n):
    lista = []
    for x in range(n):
        lista.append(input('Digite a letra que deseja adcionar: '))

    return lista

L1 = criarlista(3)  # z, c, a

L2 = list(L1)  # Cópia rasa
L3 = L1[:]

print(L1)  # ['z', 'c', 'a']
print(L2)  # ['z', 'c', 'a']
print(L3)  # ['z', 'c', 'a']

print('----------------------------')

print(L1 is L2)  # False
print(L1 is L3)  # False
print(L2 is L3)  # False

print('----------------------------')

L1.sort()

print(L1)  # ['a', 'c', 'z']
print(L2)  # ['z', 'c', 'a']
print(L3)  # ['z', 'c', 'a']

print('----------------------------')

L1[0] = 8

print(L1)  # ['8, 'c', 'z']
print(L2)  # ['z', 'c', 'a']
print(L3)  # ['z', 'c', 'a']