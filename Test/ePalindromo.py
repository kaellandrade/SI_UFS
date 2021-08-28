'''
Verifica se uma palavra é palindromo
'''
def isPalin(palavra:str, esq:int, dir:int)->bool:
    if(esq >= dir):
        return True
    elif(palavra[esq] != palavra[dir]):
        return False
    else:
        return isPalin(palavra, esq+1, dir-1)

def palin(palavra:str):
    return isPalin(palavra, 0, len(palavra)-1);
