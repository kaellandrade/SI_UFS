from math import ceil, pow


def func(x): return 2*x - 35


def encontraAB(b, fdX):
    if(fdX(b) >= 0):
        return encontraX(fdX, b//2, b)
    else:
        return encontraAB(2*b, fdX)


def encontraX(fdX, a, b) -> int:
    baixo = a
    alto = b
    while(baixo <= alto):
        m = ceil((baixo+alto)/2)

        if(fdX(m) < 0):
            baixo = m + 1
        elif(fdX(m) > 0):
            alto = m-1
        else:
            return m + 1

    return m + 1


print(encontraAB(1, func))
