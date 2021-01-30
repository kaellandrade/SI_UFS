/*
NÍVEL: Médio
Tópicos: estrutura de dados, Árvore 

Descrição
---------
Em estrutura de dados, chama-se de Árvore Binária Completa de grau D uma árvore em que todos os nós (exceto as folhas) possuem dois filhos e todas as folhas estão no mesmo nível D, sendo D a altura da árvore.

Por exemplo:
(7(13(0()())(1()()))(11(2()())(9()())))
          7
         / \
        /   \
       /     \
      /       \
     13       11
    / \       /\
   /   \     /  \
  0     1   2    9

Esta árvore binária é completa de grau = 2 pois todos os nós possuem dois filhos (exceto as folhas), todas as folhas estão no mesmo nível e a altura da árvore é 2 (a altura na raíz é 0).

Sua tarefa é simples. Dada uma árvore binária em notação de parêntese, verifique se ela é completa ou não. Se for, informe o total de nós da árvore. Caso contrário, informe quais nós tem apenas um filho.

Formato de entrada
------------------

A entrada consiste de uma linha contendo a string da árvore em notação de parênteses.

Formato de saída
----------------

A saída consiste de duas linhas:
A primeira linha contém a mensagem "completa" caso a árvore binária seja completa e "nao completa", caso contrário.
Na segunda linha, deve-se exibir:
    Caso a árvore seja completa: a mensagem "total de nos: N" onde N é um inteiro representando o total de nós na árvore
    Caso a árvore não seja completa: a mensagem "nos com um filho: N1 N2 N3 ... Ni", onde cada Ni é o inteiro que representa o nó. (N1, N2, N3, ... , Ni estão in ordem).
Cada linha deve conter um caractere de quebra de linha no final
Observe que na impressão da lista de nós, todos os nós estão separados por um caractere de espaço exceto o último nó.
*/

