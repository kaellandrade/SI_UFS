/*
Descrição
--------
O objetivo deste exercício é implementar o TAD conjunto numérico baseado em  uma Hash Table aberta usando listas encadeadas. Esse conjunto deve suportar as seguintes operações:

1. ADD(S, k) = adiciona o elemento k ao conjunto S, retornando True se o elemento foi corretamente adicionado ou false se o elemento já pertencia ao conjunto.
2. DEL(S, k) = remove o elemento k do conjunto S, retornando True se o elemento foi corretamente removido ou False se o elemento não pertencia ao conjunto.
3. HAS(S, k) = retorna True se o elemento k pertence ao conjunto S ou false se o elemento não pertence ao conjunto.

Os detalhes de implementação da Hash Table T são os seguintes:

1. Tamanho da tabela: a tabela deve ter uma capacidade inicial m=7.
2. Função de dispersão: deve ser usada a heurística da divisão, i.e. h(k)=k mod m
4. Inserção: os registros devem ser armazenadas em uma lista na posição correspondente. As inserções devem ser sempre realizadas no início da lista.
3. Fator de carga: O fator de carga a=n/m deve ser mantido em a<0.75. Assim que a>=0.75, todos os elementos da tabela atual devem ser redistribuidos (rehashing) numa nova tabela de tamanho 2*m-1 por ordem de posição na tabela corrente, ou seja, todos os elementos da lista em T[0] são realocados, do primeiro ao último elemento dessa lista, depois os da lista em T[1], na mesma ordem, e assim por diante até a lista T[m-1]. IMPORTANTE: essa verificação deve ser feita imediatamente *após* a inserção de cada novo elemento na tabela.

Formato de entrada
------------------

O arquivo de entrada consiste em uma sequência de w operações (conceitualmente numeradas de 0 a w-1), sendo uma por linha. As operações possíveis são as seguintes:

ADD k = adiciona o elemento k
DEL k = remove o elemento k
HAS k = indica se o elemento k pertence ao conjunto
PRT   = imprime alguns dados sobre a tabela (ver na descrição da saída)

Limites:
1 <= w <= 100000
0 <= k < 2^20

Formato de saída
----------------
Para cada operação (numerada i=0,...,w-1) no arquivo de entrada, deve ser impresso o resultado correspondente sobre o conjunto, conforme descrito a seguir.

a) ADD k: imprime a linha
i r c
onde
i = número da operação
r = resultado da operação (1=True, 0=False)
c = número de comparações feitas (posições da lista visitadas) até a inserção (ou não) do valor correspondente, antes de um eventual rehashing


b) DEL k: imprime a linha
i r c
onde
i = número da operação
r = resultado da operação (1=True, 0=False)
c = número de comparações feitas (posições da lista visitadas) até a remoção (ou não) do valor correspondente


c) HAS k: imprime a linha
i r c
onde
i = número da operação
r = resultado da operação (1=True, 0=False)
c = número de comparações feitas (posições da lista visitadas) até a localização (ou não) do valor correspondente

d) PRT: imprime a linha
i m n l
onde
i = número da operação
m = tamanho (capacidade da tabela)
n = número de elementos da tabela (cardinalidade do conjunto)
l = comprimento da maior lista da tabela (posição com mais elementos)
*/