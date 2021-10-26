def rotVector(x: list) -> int:
    baixo = 0
    alto = len(x) - 1

    while(baixo <= alto):
        meio = (baixo+alto)//2
        if(x[meio] < x[alto]):
            alto = meio
        else:
            baixo = meio + 1

    return meio


print(rotVector([7, 9, 15, 2, 4]))
