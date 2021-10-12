def rabin_karp_MATCHER(texto, padrao, d=256, q=3354393):
    D = d  # Tabela ASCII
    N = len(texto)
    M = len(padrao)
    h = pow(d, M-1) % q
    p = 0  # Valor hash para o padrão
    t = 0  # Valor hash para o texto

    for i in range(M):  # Pré-Processamento
        p = (d*p + ord(padrao[i])) % q
        t = (d*t + ord(texto[i])) % q

    for s in range(N-M+1):
        if(p == t):
            if(padrao == texto[s:s+M]):
                print(f'Padrão o corre em {s}')
        if(s < N-M):
            t = (D*(t-ord(texto[s])*h) + ord(texto[s+M])) % q
            if(t < 0):
                t = t+q


TEXT = 'O LOBO COME BOLO, O BOLO É DO LOBO'
PAT = 'LOBO'
rabin_karp_MATCHER(TEXT, PAT)
