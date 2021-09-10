def rotVector(x: list) -> int:
    baixo = 0
    alto = len(x) - 1

    if(baixo == alto):  # Para vetor unitário
        return 0

    while(baixo <= alto):
        meio = (baixo+alto)//2
        if(x[meio] > x[meio+1]):
            return meio + 1
        if(x[meio-1] > x[meio]):
            return meio

        if(x[alto] > x[meio]):  # Decide o fatiamento do vetor
            alto = meio - 1
        else:
            baixo = meio + 1


print(rotVector([4, 5, 1, 2, 3]))
