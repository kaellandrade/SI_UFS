#!python3.8
from MinHeap import MinHeap


class NodeHoff:
    '''
    Representação da Trie de Hoffman.
    '''

    def __init__(self, simbol, freq,  left=None, right=None) -> None:
        self.simbol = simbol #Caractere.
        self.freq = freq #Frequencia.
        self.left = left #Filho Esq.
        self.right = right #Filho Dir.

    def isLeaf(self) -> bool:
        '''
            Verifica se um dado nó é folha.
        '''
        return self.left == None and self.right == None


def expand(Trie, noAtual, dadosCompc, dadosOri='') -> str:
    '''
    ENTRADA: Trie um dado nó da Trie(inicialmente será a raiz) e os dados compactados.
    SAÍDA: Os dados originais descompactados.
    '''
    if(noAtual.isLeaf()): #É folha? Então vamos pegar seu conteúdo e voltar para raiz.
        return expand(Trie, Trie, dadosCompc, dadosOri + noAtual.simbol)

    if(len(dadosCompc) == 0): #Caso Base: Quando não houver mais dados para ser descompactados.
        return dadosOri #Retorna nossos dados (string).

    newString = dadosCompc[1:] #Remove a cabeça de nossa string.
    if(dadosCompc[0] == '0'):
        return expand(Trie, noAtual.left, newString, dadosOri) #Vamos à esquerda da árvore.
    else:
        return expand(Trie, noAtual.right, newString, dadosOri) #Vamos à direita.


def buildCodeTable(Nodex) -> dict:
    '''
    ENTRADA: Uma árvore Huffman.
    SAÍDA: Tabela de codificação.
    Controi nossa tabela de codificação de forma recursiva dado uma árvore Huf.
    '''
    def buildCodeTablesRec(tableCode, Nodex, s):
        if(Nodex.isLeaf()):
            tableCode[Nodex.simbol] = s
            return
        else:
            buildCodeTablesRec(tableCode, Nodex.left, s + '0')
            buildCodeTablesRec(tableCode, Nodex.right, s + '1')
    
    tableCode: dict = {}
    buildCodeTablesRec(tableCode, Nodex, "")
    return tableCode




def buildTrie(frequencias) -> NodeHoff:
    '''
        ENTRADA: Tabela de frequencias no formato {'a':'101','b':'001' ...}
        Recebe as frequencias e retorna nossa Trie.
        SAÍDA: Uma árvore Hoffman (Trie)
    '''
    minPq = MinHeap(key=lambda NodeH: NodeH.freq) #Mudando o fator comparativo do MinHeap.

    for ch in frequencias: #Inserindo todos nossos símmbolos dentro do heap com suas respectiva frequencia.
        minPq.insert(NodeHoff(ch, frequencias[ch]))

    while(minPq.current_size > 1): #Construindo nossa Trie
        NodeX: NodeHoff = minPq.heap_extract_min()
        NodeY: NodeHoff = minPq.heap_extract_min()
        NodeParent = NodeHoff("\0", NodeX.freq + NodeY.freq, NodeX, NodeY)
        minPq.insert(NodeParent)
    return minPq.heap_extract_min() #O último elemento do Heap é nossa árvore.


def countFreq(string)->dict:
    '''
    ENTRADA: Um string.
    SÁIDA: Um dicionário no formato {'a':1, 'b':3, c:'0'}, onde a chave é o simbolo
    e o valor é sua frequencia na string.
    '''
    frequencia: dict = {}
    for ch in string:
        if(frequencia.get(ch) != None):
            frequencia[ch] += 1
        else:
            frequencia[ch] = 1
    return frequencia


def dataCompress(tabelaCodificacao, string) -> str:
    '''
        ENTRADA: Uma tabela de codificação (criada por buildCodeTable)
        SAÍDA: Os dados comprimidos no formato string. Ex: '0101010...'
    '''
    dados_codificados = ''
    for ch in string:
        dados_codificados += tabelaCodificacao[ch]
    return dados_codificados


STRING = 'Meu gato está observando eu tocando violão.'

freq = countFreq(STRING) #Contabilizando as frequências.
arv = buildTrie(freq) #Construindo nossa árvore

tabelaCodificacao = buildCodeTable(arv) # Criando a tabela de codificação a partir da árvore.
dados_codificados = dataCompress(tabelaCodificacao, STRING) #Codificando os dados.
recomposta = expand(arv, arv, dados_codificados) #Descomprimendo os dados.

print(f'Mensagem original: {STRING}')
print(f'Mensagem comprimida: {dados_codificados}')
print(f'Mensagem recomposta: {recomposta}')
