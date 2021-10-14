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
                print(f'Padrão o corre em {s}')
        if(s < N-M):
            t = (D*(t-ord(texto[s])*h) + ord(texto[s+M])) % q
            if(t < 0):
                t = t+q

def findWord(words, matriz):
    for word in words:
        rabin_karp_MATCHER(matriz, word)

def getVerticalWord(column:int,M:int):
    '''
        ENTRADA: Um valor inteiro representando a coluna.
        SAÍDA: Uma String formada na vertical.

    '''
    word = ''
    for i in range(0, M):
        word += MATRIZ[i][column]
    return word

def reversedString(string:str):
    '''
    ENTRADA: String S.
    SAÍDA: String S invertida.
    '''
    return string[::-1]
    
# print(getVerticalWord(10,len(MATRIZ)))
# findWord(['MACACO'], MATRIZ[2])
word_vertical = getVerticalWord(0, len(MATRIZ))
print(word_vertical)
print(reversedString(word_vertical))