def naive_string_matcher(stringT: str, stringP: str) -> int:
    n = len(stringT)
    m = len(stringP)
    for s in range(0, (n - m)+1):
        if(stringP[0:m] == stringT[s:s+m]):
            print(f'Padrão occore no deslocamento {s}')

naive_string_matcher('acaabc','aab');
