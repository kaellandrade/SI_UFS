3.  
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
            se qt1 > qt0 então
                retorne False
            senão
                se(i<=n) então
                    se(x[i] = '1') então
                        retorne binary(stringBinaria, i+1, n, qt0, qt1+1)
                    senão
                        retorne binary(stringBinaria, i+1, n, qt0+1, qt1)
            retorne contZeroOne(stringBinaria, n)
        fim
        ```
    c)Complexidade
        contZeroOne é O(n) e o espaço utilizado é proporcinal à string, ou seja, 1byte*n + 4bytes(para armazenar o tamanho de n.

        binary é O(n), porém ela chama contZeroOne no final. Logo, a complexidade total seria O(2n), ou O(n). O espaço consumido
        seria 1byte*n + 4bytes +4bytes + 4bytes + 4bytes.

6. 
    I) Sem gastar espaço adicional
        a) Podemos usar dois laços para realizar essa verificação. Um externo que fixa uma valor
        o qual será comparado com os próximos valores.

        b) Pseudo-code:
        ```C
        algoritmo isDuplicated(x, n)
        {- ENTRADA: Vetor x de n elementos.

        SAIDA: True quando encontra um elemento duplicado, False caso contrário.
        -}
        início
        para i = 1 até n faça
            início
                para j = i+1 até n
                    início
                        se (x[i] == x[j]) então
                            retorne True
                    fim
            fim
        retorne False
        fim
        ```
        c) Complexidade.
            Para cada valor x temos que isDuplicated irá percorrer n-1 vez o vetor novamente.
            Logo a complexidade seria, O(n²)
            Além disso, o espaço utilizado será proporcinal ao tamanho de do vetor de entrada (n*4Bytes)
    
    II) Podendo gastar espaço adicional
        a) Para aprimorar o tempo de execução do algoritmo entarior, podemos utilizar uma tabela Hash com tamanho n,
        onde n seria o tamanho de entrada do vetor. Sendo que cada chave dessa tabela será todos os valores do vetor de entrada,
        e o valor de cada chave será justamente o total de vezes que esse valor foi encontrado.

        b) Pseudo-code:
        ```C
        algoritmo isDuplicatedWithHash(x, n)
        {- ENTRADA: Vetor x de n elementos.

        SAIDA: True quando encontra um elemento duplicado, False caso contrário.
        -}
        início
        hashTable := Null
        para i = 1 até n:
            início
                hashTable[i] = 0;
            fim
            
        para i=1 até n faça
            hashTable[x[i]] := hashTable[x[i]] +  1
            se(hashTable[x[i]]) >= 2 então
                retorne True
        retorne False  
        fim
        ```
        c) Complexidade.
