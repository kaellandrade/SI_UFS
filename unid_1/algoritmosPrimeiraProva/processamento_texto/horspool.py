def shifttable(padrao: str):
    '''
    Entrada: Padrão P [0..m - 1] e um alfabeto de caracteres possíveis.
    Saída: Tabela [0..size - 1] indexada pelos caracteres do alfabeto e
           preenchido com tamanhos de deslocamento calculados.
    '''
    tabela = [len(padrao)]*256  # Alfabeto 255 caracters. Tabela ASCII
    for i in range(len(padrao)-1):
        tabela[ord(padrao[i])] = len(padrao) - 1 - i

    return tabela


def horspoolMatching(texto, padrao):
    '''
    Entrada: Padrão P [0..m - 1] e texto T [0..n - 1]
    Saída:O índice da extremidade esquerda da última substring correspondente.
    ou -1 caso não seja encontrado um padrão.
    '''
    tabelaPre = shifttable(padrao) #Gerando a tabela de deslocamentos.
    m = len(padrao)
    n = len(texto)
    i = len(padrao) - 1 #Posição da extremidade direita do padrão.
    while(i <= n-1):
        k = 0
        while(k <= m-1 and padrao[m-1-k] == texto[i-k]):
            k += 1
        if(k == m):
            print(f'Padrão o corre em {i-m+1}')
        i = i + tabelaPre[ord(texto[i])]

horspoolMatching('micael micael micael', 'micael')