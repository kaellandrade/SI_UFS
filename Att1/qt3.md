3. Usando indução fraca, elabore um algoritmo recursivo para calcular o maior elemento
de um vetor X de n elementos.
    
    a) Podemos estruturar o problema da seguinte forma indutiva: quando n for 1, temos um único
    elemento, logo ele é o maior.

    CASO BASE: n1=x[1];

    HIPÓTESE: Suponha que conseguimos encontrar o maior valor do vetor x para n-1 elementos.

    CASO GERAL: Agora precisamos encontrar o maior valor para n. Como o maior valor está no
    range [1,2,3 ... k-1, k], basta calcular o maior valor entre 1 ... k-1 e verificar se esse
    valor é maior do que k. Se for, então encontramos, caso contrário k é o maior valor.

    PSEUDO-CODE:
    ```C
    algoritmo maxx(x, n, maior)
    {- ENTRADA: Vetor x cujo elementos de x pertencem ao conjunto dos Reais.

    SAIDA: Maior elemento de X
    -}
    início
    se n = 1 então
        retorne maior
    senão
        se (x[n-1] >= maior) então
        retorne maxx(x, n-1, x[n-1]) --x[n-1] passa a ser o maior
        senão
            retorne maxx(x, n-1, maior)
    fim

    max(x, n, x[n]) --x[n]assume o primeiro elemento de x como maior.
    ```
5. 
a) A solução foi elaborada em duas partes para atender os itens I e II.
Primeiro, temos uma função (contZeroOne) que recebe uma string e conta a quantidade de Zeros e Uns dessa string e,
retorna True caso essa quantidade seja igual, False caso contrário.

Segundo, temos uma função (binary) recursiva exclusiva para verificar o item II.
Essa função varre a string da esquerda para direita e realiza a contagem de 1s e 0s
caso em algun momento a quantidade de 1s exceda a quantidade 0s naquela posição, então retornamos False.
Porém essa função não garante a validade do item I, logo precisamos invocar contZeroOne no final.

b)Pseudo-code:
    ```C
    algoritmo contZeroOne(stringBinaria, n)
    {- ENTRADA: Vetor de carácteres e seu respectivo tamanho.

    SAIDA: True quando a quantidade de 0s e 1s forem iguais, false caso contrário.
    -}
    início
    totalZeros := 0
    totalUns := 0 
    para i = 1 até n:
        início
            se stringBinaria[i] == '0':
                totalZeros := totalZeros + 1
            else:
                totalUns := totalUns + 1
        fim
    retorne totalUns == totalZeros
    fim
    ```

    ```C
    algoritmo binary(stringBinaria, i, n, qt0, qt1)
    {- ENTRADA: Vetor de carácteres, posição inicial da string, tamanho da string, quantidade de 0s e quantidade de 1s,
    respectivamente.

    SAIDA: True se caso seja uma strnig binária válida, false caso contrário.
    -}
    início
            se qt1 > qt0:
        return False
    elif (i <= n):
        if(x[i] == '1'):
            return binary(x, i+1, n, qt0, qt1+1)
        else:
            return binary(x, i+1, n, qt0+1, qt1)
    return contZeroOne(x, len(x))
    fim
    ```