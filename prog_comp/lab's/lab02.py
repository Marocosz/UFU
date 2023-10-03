aux = True

while aux:
    qt = int(input('Digite quantos números voce deseja analisar (mais ou igual à 10) '))
    lista_num = []

    if qt < 10:

        qt = int(input('Digite quantos números voce deseja analisar (mais ou igual à 10) '))

    else:
        for x in range(qt):
            num = int(input(f'Digite o {x + 1}º número: '))
            lista_num.append(num)

        maior = max(lista_num)

        print(f'O maior número entre os números: {lista_num} é: {maior}')

        aux = False
