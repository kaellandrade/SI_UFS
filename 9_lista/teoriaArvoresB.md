# 9 Lista teoria Árvores B
1. Na inserção de uma nova chave em uma folha de uma Árvore B, o que acontece se o nó esta cheio ? Explique sua resposta

- Uma nova folha deve ser criada de tal forma que metade das chaves da folha cheia 
    seja distribuidas para nova folha recém criada. Porém, a última chave da folha velha dever ser promovida.

2. Na remoção de uma chave em uma Árvore B, o que preciso tomar cuidado em relação a quantidade de chaves do nó? Explique em uma linha.

- É preciso evitar que qualquer nó esteja menos da metade ocupado.

3. Considerando os termos “Árvores m-árias”, “Árvores binárias busca”, “Árvores de busca m-árias”, “Árvores binárias”, organize e rediga qual é relação entre estes termos e finalmente qual é propósito em comum.

- ÁRVORES M-ÁREAS são árvores múltiplas de ordem m. Isso siginifica que cada nó possui m filhos, diferente das ÁRVORES BINÁRIAS
a qual permite no máximo dois filhos. Porém, ambas tem operações bem parecidas. As ÁRVORES DE BUSCA M-ÁRIAS estão para as ÁRVORES M-ÁRIAS assim como ÁRVORES BINÁRIAS DE BUSCAM estão para as ÁRVORES BINÁRIAS. Árvores binárias de busca são eficientes para trabalhar em memória volátil (RAM), já árvores de buscam m-áreas são eficientes para trabalhar em disco rígido(HD

4. No caso da complexidade na busca em uma Árvore B o que podemos interpretar da relação entre “n” e “h” em h<=log_q( (n+1)/2 ) + 1 ? 

- Podemos concluir que para uma árvore de ordem m extremamente grande a altura de nossa árvore será bem pequena para um dado conjunto de chaves armezanado na árvore B. 

5. Na inserção de uma nova chave em uma Árvore B, a chave pode ser inserida em algum nó que está no meio da árvore, isto é, em um nó que não seja folha ? Explique sua resposta.

- Não. Pois as árvores B são construídas da base para cima, ou seja, em sequencias de inserções a raíz está em constante mudança. Essa técnica de inserir o elemento na folha possibilita que estejamos sempre com nossa Árvore B balanceada.

6. Quando falamos de uma árvore de busca m-ária com m = 2 estamos nos referindo a qual tipo de árvore em específico? Explique sua resposta.

- Uma árvore de ordem 2, ou seja, cada nó carrefa 2 filhos e, apenas uma chave. É o caso da árvore binária em específico.

7. Na Inserção de uma nova chave em uma Árvore B, especificamente quando um nó está cheio, por que uma chave deve ser promovida para o ascendente ? Explique sua resposta.

- Pois é necessário conectar o novo nó criado à arvore. Dessa forma, essa chave promovida será um novo separador de nó.

8. Qual é o problema semelhante que tem as Árvores de busca m-árias e as Árvores binárias de Busca ? Explique sua resposta. 

- Ambas podem ficar desbalancedas, e sabemos que isso é um problema para busca de um determinado elemento na estrutura de Árvore.

9. Em uma Árvore B, por que o tamanho de cada nó é importante ? Explique sua resposta.

- Porque a quantidade de informação armazenada em cada nó pode ser suficientimente tão grande a ponto de precisar poucas buscas em disco magnéticos. Dessa forma, podemos ler o máximo de informação assim que a cabeça de litura do disco estiver posicionada. (Isso levando em consideração os discos mágnéticos, hd por exemplo)

10. Na inserção de uma nova chave em uma Árvore B o que é garantido em relação ao número de chaves em cada nó ? Explique sua resposta.

- E garantido que cada folha nunca tenha menos de teto(m/2) - 1 chaves, ou seja, isso significa que cada nó está pelo menos 50% cheio. E isso é importante para deixar a árvore bem balanceada.

11. A raiz de uma Árvore B sempre tem pelo menos duas subárvores? Explique sua resposta.

- Sim, execeto que ela seja uma folha.

12. Comente cada linha de código, indicando a importância para o funcinamento do algoritmo como um todo.

 1. LINHA-> Uma função que retorna um ponteiro de uma determinada chave K, caso ela exista na Árvore B.

 2. LINHA-> Verifica se o nó está vazio;

 3. LINHA-> Realiza a iteração em cada chave de do nó a procura de K;

 4. LINHA-> Caso não encontre o chave no nó atual, será passado para o próximo nó (LINHA 5) , caindo novamente nas linhas 1, 2, 3 de forma recursiva.

 6. Caso contrário, significa que encontramos nossa chave, retornando assim nosso node.

 7. Será executada se a chave k não for encontrada.

13. Por que uma Árvore B é dita perfeitamente Balanceada ? Explique sua resposta.
- Pois todos os nós folhas se encontram no mesmo nível da Árvore B.

14. Em uma Árvore B, qual é a propiedade que indica que esta árvore está sempre cheia até a metade pelo menos.
- Teto(m/2) <= k <=m

15. Na remoção de uma chave em uma Árvore B, em que situação será necessária fundir os nos ? 
- Quando o seu ascendente é uma raiz com apenas uma chave. Nesse caoso as chaves do nó irmãos passarão para raiz.

16. Na Inserção de uma nova chave em uma Árvore B, especificamente quando um nó está cheio, e após a divisão e distribuição das chaves o que acontece se nó não era raiz ?

17. Em uma Árvore B, explique o que subutilização. 

18. Descreva melhor e com palavras o pior caso de busca em uma Árvore B.
