def fancy_fence() -> None:
    t = int(input())
    while t:
        a = int(input())
        print(isImpossible(a))
        t -= 1


def isImpossible(a: int) -> str:
    def formula(a): return 360 % (180-a) == 0
    if(formula(a)):
        return 'YES'
    else:
        return 'NO'


fancy_fence()
