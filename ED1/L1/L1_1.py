n = input("Digite um número, e se quiser parar digite 'parar': ")
maior = float('-inf')

while True:
    n = input("Digite um número, e se quiser parar digite 'parar': ")
    if n == 'parar':
        break
    else:
        if int(n) > maior:
            maior = int(n)

print(maior)