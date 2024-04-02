from avl import *
import time

tree = AVL()

with open('as_andorinhas.txt', mode='r', encoding='utf-8') as arq:
    cont = 1
    palavras_distintas = 0
    palavras_totais = 0
    palavras_descartadas = 0

    tempo_inicio = time.time()
    for line in arq:
        for word in line.split():
            word = "".join(c for c in word if c.isalpha())
            word = word.lower()
            if len(word) > 1:
                if tree.busca(word) is False:
                    tree.insere(word, str(cont))
                    palavras_distintas += 1
                    palavras_totais += 1
                else:
                    tree.insere_lista_linha(word, str(cont))
                    palavras_totais += 1
            else:
                palavras_descartadas += 1

        cont += 1
    tempo_fim = time.time()

tempo_construcao = round(tempo_fim - tempo_inicio, 15)

tree.emOrdem()
indice = tree.arqtxt
rotacoes_ll_rr = tree.rotacoes_ll_rr
rotacoes_lr_rl = tree.rotacoes_lr_rl



with open('indices.txt', 'w', encoding='utf-8') as narq:
    narq.write(f'Índice:\n')
    for linha in indice:
        narq.write(f'{linha}\n')

    narq.write(f'Total de palavras: {palavras_totais}\n')
    narq.write(f'Total de palavras distintas: {palavras_distintas}\n')
    narq.write(f'Total de palavras descartadas: {palavras_descartadas}\n')
    narq.write(f'Tempo de construção da árvore: {tempo_construcao} segundos\n')
    narq.write(f'Total de rotações LL e RR: {rotacoes_ll_rr}\n')
    narq.write(f'Total de rotações LR e RL: {rotacoes_lr_rl}\n')