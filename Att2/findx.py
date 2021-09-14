from math import floor


def rotVector(x: list) -> int:
    # def f_x(y): return 4*y-40
    # def f_x(y): return 2*y-35
    # def f_x(y): return 9*y-90
    def f_x(y): return y*9-60
    baixo = 0
    alto = len(x) - 1

    while(baixo < alto):
        x1 = (baixo+alto)//2

        if(f_x(x[x1]) < 0):
            baixo = x1 + 1
        elif(f_x(x[x1]) > 0):
            alto = x1-1
        else:
            return x1 + 1

    return x1+1


print(rotVector([x for x in range(0, 8)]))
