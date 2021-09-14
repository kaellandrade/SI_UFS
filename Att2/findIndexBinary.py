def rotVector(x: list) -> int:
    baixo = 0
    alto = len(x) - 1

    while(baixo <= alto):
        meio = (baixo+alto)//2
        if(x[meio] == meio):
            return meio

        if(x[meio] < meio):
            baixo = meio + 1
        else:
            alto = meio - 1

    return -1


print(rotVector([-10, -3, -2, 0, 4]))
