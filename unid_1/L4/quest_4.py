''' REPRESENTAÇÃO ORIGINAL
L M O C R O P B G C A
E M Y K V A C A G A L
B M A C A C O M A L P
R L L M A T N G A M A
E L E P A T N M A C T
O U R S T I F O C C O
M R U Y Y T X Z E B R
N A U T I C H Z A T C
P A M E L H E U S A A
Y L U L H A B I U S L
B C V A B E L H A B A
'''
# TODO: VERIFICAR A PALAVRA CROTA.

MATRIZ = [
    "LMOCROPBGCA",
    "EMYKVACAGAL",
    "BMACACOMALP",
    "RLLMATNGAMA",
    "ELEPATNMACT",
    "OURSTIFOCCO",
    "MRUYYTXZEBR",
    "NAUTICHZATC",
    "PAMELHEUSAA",
    "YLULHABIUSL",
    "BCVABELHABA"
]


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
                return s
        if(s < N-M):
            t = (D*(t-ord(texto[s])*h) + ord(texto[s+M])) % q
            if(t < 0):
                t = t+q
    return -1


def findWord(words, matriz):
    for word in words:
        for i in range(0, len(MATRIZ)):
            if(i == 0):
                for column in range(len(matriz)):
                    word_vertical = getVerticalWord(column, len(matriz))
                    word_vertical_rever = reversedString(word_vertical)

                    res_vertical = rabin_karp_MATCHER(word_vertical, word)
                    res_vertical_rever = rabin_karp_MATCHER(
                        word_vertical_rever, word)
                    if(res_vertical != -1):
                        print((word, (res_vertical, column),
                              (res_vertical+len(word)-1, column)))

                    if(res_vertical_rever != -1):
                        print((word, (len(word_vertical_rever)-res_vertical_rever-1, column),
                              (abs((res_vertical_rever+len(word)) - len(word_vertical_rever)), column)))

            res = rabin_karp_MATCHER(matriz[i], word)
            revers_horizon = rabin_karp_MATCHER(
                matriz[i], reversedString(word))

            if(revers_horizon != -1):
                print((word, (i, revers_horizon+len(word)-1),
                       (i, revers_horizon)))

            if(res != -1):
                print((word, (i, res), (i, res+len(word)-1)))


def getVerticalWord(column: int, M: int):
    '''
        ENTRADA: Um valor inteiro representando a coluna.
        SAÍDA: Uma String formada na vertical.
    '''
    word = ''
    for i in range(0, M):
        word += MATRIZ[i][column]
    return word


def reversedString(string: str):
    '''
    ENTRADA: String S.
    SAÍDA: String S invertida.
    '''
    return string[::-1]


findWord([
    'PATO',
    'MACACO',
    'LEBRE',
    'VACA',
    'PORCO',
    'ORCA',
    'ABELHA',
    'MEL',
    'CROTA',
    'OCCO',
    'LAY',
    'LIYTA'
], MATRIZ)
