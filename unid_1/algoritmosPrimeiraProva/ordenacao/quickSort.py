def quickSort(lista, l=0, r=None):
    if (r is None):
        r = len(lista) - 1
    if(l < r):
        s = partition(lista, l, r)
        quickSort(lista, l, s-1)
        quickSort(lista, s+1, r)


def partition(lista, l, r):
    p = lista[r]
    i = l
    for j in range(l, r):
        if lista[j] <= p:
            lista[i], lista[j] = lista[j], lista[i]
            i+=1
    lista[i], lista[r] = lista[r], lista[i]
    return i


A = [10,9,8,7,6,5,4,3,2,1, 10]
quickSort(A)
print(A)