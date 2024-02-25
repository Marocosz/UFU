"""
## Árvores Balanceadas

A complexidade de bsuca de uma "árvore binária de busca" seria O(h), a altura dela, porém, nessa árvore não temos como
garantir uma ótima distribuição da altura, quando num caso onde há números em sequência (parecendo uma lista e assim se
tornando uma espécie de lista), assim não sendo a mais
efieciente.

Com a árvore bem distribuida, balanceada dos dois lados e [completa], temos que a complexidade de busca seria O(ln(N))

OBS: É importante salientar que em alguns casos para remover ou inserir um ítem na árvore, poderiamos ter uma
complexidade o(N) quando formos balancear novamente. E para resolver isso, devemos relaxar um pouco as restrições em
questão da árvore ser completa, assim podemos denotar que a árvore seja proporcional a log(N). Ou seja, nem toda árvore
balanceada é uma árvore completa.
"""

"""
## Árvore AVL (Adeslson-Vesky e Landis)

É uma árvore binária de busca, com a propriedade onde a diferença de altura da subárvore da esquerda com a subárvore da
direita seja apenas 1 (fato de balanço)

Com isso, a Árvore AVL tem uma propriedade de rotação, para balancear a estrutura
"""