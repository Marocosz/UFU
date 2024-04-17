"""
Exercío 01

1: A função não é boa devido a grande chance de repetição desses valores que serão utilizados como posição
assim, podendo ter conflito de informações guardadas

2: Ao haver um nome com muitas letras, haveria muita soma, além de gastar mais processamento, o índice estaria
muito distante

3: Resultado "530" para os dois

4: Lista com tamanho 4

"""


def teste_hash(palavra):
    return sum([ord(letra) for letra in palavra])


print(teste_hash("marco"))
print(teste_hash("carmo"))

"""
Exercício 2:
"""


def novo_teste_hash(palavra):
    lista_palavra = palavra.split(" ")
    nova_palavra = "".join(lista_palavra)

    return sum([ord(letra) for letra in nova_palavra])


print(teste_hash("marco antonio"))
print(novo_teste_hash("marco antonio"))


"""
Exercício 3
"""


def menor_teste_hash(palavra):
    return sum([ord(letra) for letra in palavra.lower()])


print(teste_hash("MARCOS"))
print(teste_hash("marcos"))
print(menor_teste_hash("MARCOS"))

"""
Exercício 4
"""


def vogais_teste_hash(palavra):
    cont = 0
    vogais = ['a', 'á', 'à', 'â', 'ã', 'A', 'Á', 'À', 'Â', 'Ã', 'e', 'é', 'è', 'ê', 'E', 'É', 'È', 'Ê', 'i',
              'í', 'ì', 'î', 'I', 'Í', 'Ì', 'Î', 'o', 'ó', 'ò', 'ô', 'õ', 'O', 'Ó', 'Ò', 'Ô', 'Õ', 'u', 'ú',
              'ù', 'û', 'U', 'Ú', 'Ù', 'Û']

    lista_palavra = []

    for vogal in vogais:
        if vogal not in palavra:
            cont += 1

    if cont == len(vogais):
        return -1

    for letra in palavra:
        if letra not in vogais:
            lista_palavra.append(letra)

    nova_palavra = "".join(lista_palavra)

    return sum([ord(letra) for letra in nova_palavra])


print(teste_hash("Marcos Rodrigues"))
print(vogais_teste_hash("Marcos Rodrigues"))
print(teste_hash("Ls Lm"))
print(vogais_teste_hash("Luis Lima"))


"""
Exercício 5
"""


def teste_hash(palavra, M):
    nro = sum([ord(letra) for letra in palavra])
    ind = nro % M   # resto da divisão por M
    return ind


print("==================================================================================")
listanomes = ["Luiz Lima", "Ana Silva", "Caio Faria", "Sara Alves", "Joao Augusto"]

[print(teste_hash(nome,11)) for nome in listanomes]
print("==================================================================================")
[print(teste_hash(nome,7)) for nome in listanomes]
print("==================================================================================")
[print(teste_hash(nome,9)) for nome in listanomes]

"""
Conseguimos ver que os valores retornados são diferentes em cada caso, visto que o número vai ser 
diferente de acordo com o tamanho da tabela, e dessa forma, criamos uma especie de intervalo
que conseguimos "controlar" as informações dos dados
"""