n = input("Digite um número, e se quiser parar digite 'parar': ")
lista = []

while True:
    n = input("Digite mais um número: ")
    if n == "parar":
        break
    lista.append(float(n))

maior = max(lista)

print(f"O maior número dado é: {maior}")