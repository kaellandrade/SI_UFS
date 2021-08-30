
def isDuplicatedWithHash(x: list, n: int,) -> bool:
    count = {x[i]: 0 for i in range(0, n)}
    for i in range(0, n):
        count[x[i]] += 1
        if(count[x[i]]) >= 2:
            return True

    return False


vet = [1, 2, 3, 4, 3, 6]

print(isDuplicatedWithHash(vet, len(vet)))


# def isDuplicated(x: list, n: int,) -> bool:
#     for i in range(0, n):  # O(n)
#         for j in range(i+1, n):  # O(n)
#             if(x[i] == x[j]):  # O(1)
#                 return True  # O(1)
#     return False  # O(1)


# vet = [1, 2]

# print(isDuplicated(vet, len(vet)))
