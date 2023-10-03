p1 = input('Digite a primeira palavra: ')
p2 = input('Digite a segunda palavra: ')

ap1 = p1
ap2 = p2

tam_p1 = 0
tam_p2 = 0

while p1:
    p1 = p1[1:]
    tam_p1 += 1

while p2:
    p2 = p2[1:]
    tam_p2 += 1

if ap1 == ap2:
    print(f'São palavras iguais')
    
else:
    if tam_p1 > tam_p2:
        print(f'A maior das duas palavras é: {ap1}, com {tam_p1} letras')

    elif tam_p1 == tam_p2:
        print(f'As palavras: {ap1} e {ap2}, possuem o mesmo tamanho')

    else:
        print(f'A maior das duas palavras é: {ap2}, com {tam_p2} letras')