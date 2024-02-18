"""
## Complexidade: É a medida da quantidade de recursos, de eficiência, de um algorítmo

Algorpítmo: Um algorítmo tem dois grandes fatores para determinar sua eficiência, sendo elas:

Complexidade de Espaço (Memória) -> Quantidade de variáveis, elementos (brutamente falando)
Complexidade de Tempo (Processamento) -> Quantidade de operações elementares do algorítmo (atribuções, cálculos, ...)

A Complexiade do Algorítmo é bastante influenciado pela entrada dos dados dele

OBS: Sempre analisamos a complexidade do algorítmo diante o pior caso possível

## Notação do O Grande:
Usamos ele para facilitar a análise, buscamos "excluir" as variáveis fixas do cáluclo, deixando a função apenas em
função do "N" sendo "N" a entrada do algorítmo (uma lista por exemplo).
Buscamos sempre o "termo dominante" (Aquele na função cujo há a maior efetividade no aumento do resultado)

Exemplo: A Função de complexidade do algorítmo sendo: N*(N-1)/2 (Soma entre os termos de uma PA)
Temos que: N*(N-1)/2 = (N^2 - N)/2 -> Assim, sabemos que o termo dominante é "N^2"
Em termos da notação do O Grande, ficaria: O(N^2)

Assim, usando essa análise do O Grande, conseguimos destinguir melhor a complexiade entre os algorítmos


"""