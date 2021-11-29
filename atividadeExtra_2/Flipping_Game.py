def flipping_Game():
    n = int(input())
    lista = list(map(int, input().split(' ')))
    total_1s = 0
    resp = 0
    x = 0
    for i in range(n):
        total_1s += lista[i]
        if(lista[i] == 1):
            lista[i] = -1
        else:
            lista[i] = 1
    if(total_1s == n):
        print(total_1s - 1)
        return
    for i in range(0, n):
        x = max(x+lista[i], 0)
        resp = max(x, resp)
    print(resp+total_1s)
flipping_Game()
