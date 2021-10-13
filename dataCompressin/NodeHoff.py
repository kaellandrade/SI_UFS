#!python3.8
from MinHeap import MinHeap

# it was the best of times it was the worst of times (Exemplo para contrução)


class NodeHoff:
    '''
    Representação da Trie de Hoffman
    '''

    def __init__(self, simbol, freq,  left=None, right=None) -> None:
        self.simbol = simbol
        self.freq = freq
        self.left = left
        self.right = right

    def isLeaf(self) -> bool:
        return self.left == None and self.right == None

    def compareTo(self, nod) -> int:
        return self.freq - nod.freq


def expand(Trie, dadosCodificados) -> None:
    root = Trie
    noAtual = Trie
    resposta = ""
    for i in range(0, len(dadosCodificados)):
        if(dados_codificados[i] == '0'):
            noAtual = noAtual.left
        else:
            noAtual = noAtual.right
        if(noAtual.isLeaf()):
            resposta += noAtual.simbol
            noAtual = root
    return resposta


def buildCode(Nodex):
    # Building an encoding table from a (prefix-free) code trie
    st: dict = {}
    buildCodeseRec(st, Nodex, "")
    return st


def buildCodeseRec(st, Nodex, s):
    # Building an encoding table from a (prefix-free) code trie
    if(Nodex.isLeaf()):
        st[Nodex.simbol] = s
        return
    else:
        buildCodeseRec(st, Nodex.left, s + '0')
        buildCodeseRec(st, Nodex.right, s + '1')


def storeCodes(root, s=''):
    # Building an encoding table from a (prefix-free) code trie
    if(root == None):
        return

    if(root.simbol != '\0'):
        print(f'{root.simbol}: {s}')

    storeCodes(root.left, s + '0')
    storeCodes(root.right, s + '1')


def buildTrie(frequencias):
    minPq = MinHeap(key=lambda NodeH: NodeH.freq)
    for ch in frequencias:
        minPq.insert(NodeHoff(ch, frequencias[ch]))
    while(minPq.current_size > 1):
        NodeX: NodeHoff = minPq.heap_extract_min()
        NodeY: NodeHoff = minPq.heap_extract_min()
        NodeParent = NodeHoff("\0", NodeX.freq + NodeY.freq, NodeX, NodeY)
        minPq.insert(NodeParent)
    return minPq.heap_extract_min()


def countFreq(string):
    '''
    Contabiliza as frequencias.
    '''
    frequencia: dict = {}
    for ch in string:
        if(frequencia.get(ch) != None):
            frequencia[ch] += 1
        else:
            frequencia[ch] = 1
    return frequencia


STRING = '''
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
'''
freq = countFreq(STRING)
arv = buildTrie(freq)

# expand(arv)
tabelaCodificacao = buildCode(arv)
dados_codificados = ''
for ch in STRING:
    dados_codificados += tabelaCodificacao[ch]

print(dados_codificados)
print(expand(arv, dados_codificados))
