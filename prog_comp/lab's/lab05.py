dividendo = int(input("Digite o divdendo: "))
divisor = int(input("Digite o divisor: "))

dividendo_1 = dividendo

quociente = 0

if divisor == 0:
    print("Não existe divisão por 0!")


if dividendo > 0:
    if divisor > 0:
        while dividendo_1 >= divisor:
            dividendo_1 -= divisor
            quociente += 1

        print(f"Ao dividir {dividendo} por {divisor}, achamos o quociente: {quociente} e o resto {dividendo_1}")

    if divisor < 0:
        divisor = divisor * -1
        while dividendo_1 >= divisor :
            dividendo_1 -= divisor
            quociente += 1

        divisor = divisor * -1
        quociente = quociente * -1
        print(f"Ao dividir {dividendo} por {divisor}, achamos o quociente: {quociente} e o resto {dividendo_1}")


if dividendo < 0:
    dividendo_1 = dividendo_1 * -1
    if divisor > 0:
        while dividendo_1 >= divisor:
            dividendo_1 -= divisor
            quociente += 1

        dividendo_1 = dividendo_1 * -1
        quociente = quociente * -1
        print(f"Ao dividir {dividendo} por {divisor}, achamos o quociente: {quociente} e o resto {dividendo_1}")

    if divisor < 0:
        divisor = divisor * -1
        while dividendo_1 >= divisor:
            dividendo_1 -= divisor
            quociente += 1

        divisor = divisor * -1

        print(f"Ao dividir {dividendo} por {divisor}, achamos o quociente: {quociente} e o resto {dividendo_1}")
