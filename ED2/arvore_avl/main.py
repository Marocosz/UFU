from avl import AVL

V = [1, 2, 3, 10, 4, 5, 9, 7, 8, 6]
V1 = [1, 2, 3, 10, 4, 5, 5, 9, 7, 8, 6]

arv = AVL()
for v in V:
    arv.insere(v)
print('\nEm Niveis: ')
arv.emNivel()
print('\n')

arv1 = AVL()
for v in V:
    arv1.insere(v)
print('\nEm Niveis: ')
arv1.emNivel()
print('\n')

# arv.alteraValNo()
arv.espelho()
arv.emNivel()
arv.emOrdem()

R = [7, 8, 9]
for v in R:
    print('Remove: ', v)
    arv.remove(v)
    arv.emNivel()
    print('\n')