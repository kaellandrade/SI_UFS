from kmp import KMP

def shifttable(padrao: str):
    tabela = [len(padrao)]*256  # Alfabeto 255 caracters.
    for i in range(len(padrao)-1):
        tabela[ord(padrao[i])] = len(padrao) - 1 - i

    return tabela


def horspoolMatching(texto, padrao):
    tabelaPre = shifttable(padrao)
    m = len(padrao)
    n = len(texto)
    i = len(padrao) - 1
    while(i <= n-1):
        k = 0
        while(k<=m-1 and padrao[m-1-k]==texto[i-k]):
            k+=1
        if(k==m):
            print(f'Padrão em {i-m+1}')
        i = i + tabelaPre[ord(texto[i])]

TEXTO = '''
Saltar para o conteúdo
Alternar barra lateral
Wikipédia
Busca
Busca
Busca

adeSobre a WikipédiaAvisos geraisVersão móvelProgramadoresEstatísticasDeclaração sobre ''cookies''Wikimedia FoundationPowered by MediaWiki
'''
PADRAO = 'Busca'


print('horspoolMatching:')
horspoolMatching(TEXTO, PADRAO)

print('\nKMP')
KMP(TEXTO,PADRAO);