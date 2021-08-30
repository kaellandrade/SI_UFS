from util import calculateTime


def isDuplicatedWithHash(x: list, n: int,) -> bool:  # O(n)
    count = {x[i]: 0 for i in range(0, n)}  # O(n)
    for i in range(0, n):  # O(n)
        count[x[i]] += 1  # O(1)
        if(count[x[i]]) >= 2:  # O(1)
            return True  # O(1)

    return False  # O(1)


x1 = [x for x in range(0, 10000)]
# print(isDuplicatedWithHash(x1, len(x1)))

print(calculateTime.calcTime(lambda: isDuplicatedWithHash(x1, len(x1))))


def isDuplicated(x: list, n: int,) -> bool:  # O(n²)
    for i in range(0, n):  # O(n)
        for j in range(i+1, n):  # O(n)
            if(x[i] == x[j]):  # O(1)
                return True  # O(1)
    return False  # O(1)


x2 = [x for x in range(0, 10000)]

# print(isDuplicated(x2, len(x2)))
print(calculateTime.calcTime(lambda: isDuplicated(x2, len(x2))))
