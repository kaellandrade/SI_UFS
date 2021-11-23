from math import floor, inf

def berSe() -> int:
    n_meninos = int(input())
    meninos = list(map(int, input().split()))
    n_meninas = int(input())
    meninas = list(map(int, input().split()))

    meninos.sort()
    meninas.sort()
    total = 0
    for i in  range(n_meninos):
        for j in  range(n_meninas):
            if(abs(meninos[i] - meninas[j])<=1):
                meninas[j] = -inf
                total += 1
                break
    return total


print(berSe())
