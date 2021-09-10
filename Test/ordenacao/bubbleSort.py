def bubbleSort(A: list) -> list: # Analisar complexidade
    for i in range(0, len(A)-1):
        for j in range(0, len(A)-i-1):
            if(A[j] > A[j+1]):
                [A[j], A[j+1]] = [A[j+1], A[j]]
    return A

print(bubbleSort([2,3,1,2,3,0-1,10,100,0]))