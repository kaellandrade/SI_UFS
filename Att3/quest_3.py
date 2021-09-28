from Heapmax import HeapMax

TEXTO = "LOBO BOLO LOBO BOLO COMIDA LOBO HEAP HEAP-MAX HEAP-MAX HEAP-MAX LOBO"

'''
    Extrai as palavras do texto retornando uma lista de tuplas do tipo:
    (TOTAL_OCORRENCIA, PALAVRA)
'''
def extraiPalavras(texto: str) -> list:
    ocorrencia_palavra = {}
    listaTuplas = []
    for palavra in texto.split():
        if(ocorrencia_palavra.get(palavra)):
            ocorrencia_palavra[palavra] += 1
        else:
            ocorrencia_palavra[palavra] = 1

    for palavra in ocorrencia_palavra:
        listaTuplas.append((ocorrencia_palavra[palavra], palavra))

    return listaTuplas


def maisFrequentes(texto: str) -> list:
    palavras_extraidas = extraiPalavras(texto)
    HeapMax.heapSort(palavras_extraidas)
    return palavras_extraidas[len(palavras_extraidas) - 2:]

print(maisFrequentes(TEXTO))
