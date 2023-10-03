def fat(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*fat(n-1)
    
def media(lista):
    soma = sum(lista)
    media = soma/len(lista)
    return media


num = input("digite os números que deseja, e se quiser parar, digite 'parar': ")
lista1 = []

lista1.append(int(num))

while True:
    num = input('Digite outro número: ')
    
    if num == 'parar':
        break
    else:
        lista1.append(int(num))

def main():
    listacop = lista1.copy()

    print(lista1)

    listacop.sort()
    print(listacop)

    listacop.sort(reverse=True)
    print(listacop)

    lista2 = []
    for x in lista1:
        a = fat(x)
        lista2.append(a)

    lista2.sort()
    print(lista2)

    lista2.sort(reverse=True)
    print(lista2)

    print(lista1)

    med = media(lista1)
    print(med)

main()