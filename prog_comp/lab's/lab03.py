lista_num = []

n = input(f'Digite o número (se quiser parar de digitar os números digite "Sair"): ')
lista_num.append(n)

while n != 'Sair':
    n = input(f'Digite o número: ')
    lista_num.append(n)

lista_num.pop(-1)

lista_nova = []

flag = False

for x in range(len(lista_num)):

    tamanho = len(lista_nova)

    n = int(lista_num[x])

    if tamanho > 0:

        for y in range(tamanho):

            if n <= int(lista_nova[y]):
                lista_nova.insert(y, n)

                flag = True

                break

    if x == 0 or not flag:

        lista_nova.append(n)

    else:

        flag = False

print(f'Dos números: {lista_num}, ordenado são: {lista_nova}')
