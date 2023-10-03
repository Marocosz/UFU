a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a >= b:
    if a >= c:
        if b >= c:
            saida = f'{a}, {b}, {c}'
        else:
            saida = f'{a}, {c}, {b}'
    else:
        saida = f'{c}, {a}, {b}'

else:
    if a >= c:
        if b >= c:
            saida = f'{b}, {a}, {c}'
        else:
            saida = f'{c}, {b}, {a}'
    else:
        saida = f'{b}, {c}, {a}'


print(f'Ordem crescente dos números: {a}, {b}, {c} é: {saida}')
