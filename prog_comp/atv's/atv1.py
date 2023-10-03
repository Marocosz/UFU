A = int(input('Digite o valor de A: '))
B = int(input('Digite o valor de B: '))
C = int(input('Digite o valor de C: '))

MAX = None

if A > B:
    MAX = A
else:
    MAX = B

if C > MAX:
    MAX = C


print(f'O maior número entre {A}, {B} e {C} é: {MAX}')
