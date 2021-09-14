def maxProduct(vect: list) -> list:
    indexParMax = (0, 1)
    for i in range(0, len(vect)+1):
        valuePar = vect[indexParMax[0]] * vect[indexParMax[1]]
        for j in range(i+1, len(vect)):
            if(vect[i]*vect[j] > valuePar):
                indexParMax = (i, j)
    return vect[indexParMax[0]] * vect[indexParMax[1]]


print(maxProduct([5, -10, 4, 6, -2, -3, 90]))
