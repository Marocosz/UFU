dados = dict()


def criar(dic, nome):
    if nome in dic:
        print(f'{nome} já existe!')
        return nome
    else:
        valor = input('Digite o valor do gasto: ')
        return valor


def consultar(dic, nome):
    if nome in dic:
        print(f'O valor de {nome} é: {dic[nome]}')
    else:
        print(f'{nome} não existe.')


def atualizar(dic, nome):
    if nome in dic:
        valor = input('Digite o valor que deseja atualizar: ')
        dic.update({nome: valor})
        print("Atualizado com sucesso!")
    else:
        print(f'{nome} não existe.')

def deletar(dic, nome):
    if nome in dic:
        conf = input("Digite 'Sim' para confirmar a deleção: ")
        if conf == 'Sim':
            print('Deletado com sucesso!')
            del dic[nome]
        else:
            print("Confirmação não aceita.")

    else:
        print(f'{nome} não existe.')


def main(dic1):
    x = input("Digite alguma das operações CRUD: ")

    match x.title():

        case 'C':
            c = input("Digite o nome do gasto: ")
            if c in dic1:
                k = input(f'{c} já existe! Digite "R" para consultá-lo, "U" para atualizá-lo ou "D" para deletá-lo.')
                match k.title():

                    case 'R':
                        consultar(dic1, c)

                    case 'U':
                        atualizar(dic1, c)

                    case 'D':
                        deletar(dic1, c)

                    case _:
                        print('Nada foi feito')
            else:
                dic1.update({c: criar(dic1, c)})
                print("Criado com sucesso!")

            print()


        case 'R':
            r = input("Digite o nome do gasto: ")
            consultar(dic1, r)

            print()


        case 'U':
            u = input("Digite o nome do gasto: ")
            atualizar(dic1, u)

            print()

        case 'D':
            d = input("Digite o nome do gasto: ")
            deletar(dic1, d)

            print()

        case 'X':
            print("Obrigado por usar nosso aplicativo!")
            exit()

        case _:
            print('Não há essa opção')

            print()


while __name__ == '__main__':
    main(dados)
