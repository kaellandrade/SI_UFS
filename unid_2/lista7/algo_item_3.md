1. Classifique todos os itens em ordem decrescente de razão de 
    valor por unidade de peso para que um limite superior possa ser calculado usando 
    o Greedy Approach.

2. Inicialize o lucro máximo, maxProfit = 0

3. Crie uma fila vazia, Q.

4. Crie um nó fictício da árvore de decisão e enfileire-o em Q. 
O lucro e o peso do nó fictício são 0.

5. Faça o seguinte enquanto Q não estiver vazio.

    - Extraia um item de Q. Deixe o item extraído ser u.

    - Calcule o lucro do nó do próximo nível. Se o lucro for maior que maxProfit, atualize maxProfit. 

    - Limite de cálculo do nó do próximo nível. Se o limite for maior do que maxProfit, adicione o nó do próximo nível a Q.

    - Considere o caso em que o nó do próximo nível não é considerado como parte da solução e adicione um nó à fila com o nível seguinte, mas peso e lucro sem considerar os nós do próximo nível.

  