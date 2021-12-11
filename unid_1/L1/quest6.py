'''
Recebe um vetor X com n elementos e retorna True caso haja elmentos repetidos.
Cada elemento de X será uma chave da tabela Hash.
'''
def isDuplicatedWithHash(x: list, n: int,) -> bool: 
    count = {x[i]: 0 for i in range(0, n)}  
    for i in range(0, n):  
        count[x[i]] += 1  
        if(count[x[i]]) >= 2:  
            return True  
    return False  


x1 =[1, 2,5, 3, 4, 5]
print(isDuplicatedWithHash(x1, len(x1)))

'''
Recebe um vetor x com n elementos e retorna True caso
haja elementos repetidos.
'''
def isDuplicated(x: list, n: int,) -> bool:  
    for i in range(0, n):  
        for j in range(i+1, n):  
            if(x[i] == x[j]):  
                return True  
    return False  


x2 = [1, 2, 3, 4, 5, 5]
print(isDuplicated(x2, len(x2)))