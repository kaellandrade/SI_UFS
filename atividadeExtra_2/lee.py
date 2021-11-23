#!python3.8
def polygon_beautiful():
    tot_mercado = int(input())

    for i in range(tot_mercado):
        lados = int(input())
        if(is_convex(lados)):
            print('YES')
        else:
            print('NO')

def is_convex(number:int)->bool:
    return number % 4 == 0

polygon_beautiful()