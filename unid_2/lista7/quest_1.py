comb = []
k = 4
b = [0]*k
res = []


def teste(k, i, b):
    if(i == k):
        res.append(b.copy())
    else:
        for j in range(0, 10):
            b[i] = j
            teste(k, i+1, b)


def filterValisSum(l):
    soma_pares = 0
    soma_impares = 0
    if(l[0] == 0):
        return False
    for i in range(len(l)):
        if(i % 2 == 0):
            soma_pares += l[i]
        else:
            soma_impares += l[i]
    return soma_impares == soma_pares


teste(k, 0, b)
print(list(filter(filterValisSum, res)))
