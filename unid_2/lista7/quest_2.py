#!python3.8
def conjuntoPotencia(conjunto: list) -> list:
    N_ELEMENTOS = len(conjunto)
    B = [0]*N_ELEMENTOS  # Primeira combinacao possível
    bit_combinacoes = []
    conjunto_pot = []
    combinacoes(0, B, bit_combinacoes, N_ELEMENTOS)

    # Gerando o conjunto potência
    for j in range((2**N_ELEMENTOS)):
        sub_conjunto = []
        for i in range(0, N_ELEMENTOS):
            if(bit_combinacoes[j][i] == 1):
                sub_conjunto.append(conjunto[i])
        conjunto_pot.append(sub_conjunto)
    return conjunto_pot


def combinacoes(i, B, bit_combinacoes, N):
    if(i == N):
        bit_combinacoes.append(B.copy())
    else:
        B[i] = 1
        combinacoes(i+1, B, bit_combinacoes, N)

        B[i] = 0
        combinacoes(i+1, B, bit_combinacoes, N)


print(conjuntoPotencia([1,2]))
