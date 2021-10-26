def forcaBruta(stringT: str, stringP: str) -> int:
    i = 0
    j = 0
    index = -1
    while (index == -1 and i < len(stringT)):
        if(stringP[j] == stringT[i]):
            j += 1
            i += 1
        else:
            i = i-j + 1
            j = 0
        if(j == len(stringP)):
            index = i - len(stringP)
    return index

print(forcaBruta('micael andrade dos', 'dos'))