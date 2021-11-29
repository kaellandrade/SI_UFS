def Dreamoon():
    string1 = str(input())
    string2 = str(input())

    resposta_posicao = 0
    posicao_final = 0
    movimentos = 0  # Números de '?'

    for ch in string1:
        if(ch == '+'):
            resposta_posicao += 1
        else:
            resposta_posicao += -1

    for ch in string2:
        if(ch == '?'):
            movimentos += 1
        else:
            if(ch == '+'):
                posicao_final += 1
            else:
                posicao_final += -1

    distancia = resposta_posicao-posicao_final

    if((distancia+movimentos) % 2 != 0 or movimentos < abs(distancia)):
        resposta = 0
    else:
        m = (movimentos+abs(distancia))//2  # movimentos
        c = 1
        for i in range(m):
            c *= movimentos-i
        for i in range(2, m+1):
            c /= i
        resposta = c/(1 << movimentos)
    print(("{:.12f}".format(resposta)))


Dreamoon()
