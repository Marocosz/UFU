a = int(input('Digite um número: '))

L = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]

for lam in L:
    print(lam(a))