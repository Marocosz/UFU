palavra1 = input('Digite a palavra 1: ')
palavra2 = input('Digite a palavra 2: ')

qt1 = 0
qt2 = 0

for i in palavra1:
    qt1 += 1

for i in palavra2:
    qt2 += 1

if qt1 > qt2:
    print(f'A maior palavra é: "{palavra1}"')
else:
    print(f'A maior palavra é: "{palavra2}"')
