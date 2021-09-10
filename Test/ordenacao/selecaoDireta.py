def selecaoDireta(A: list) -> list:  # O(n²)
    for i in range(0, len(A)-1):
        menor = i
        for j in range(i+1, len(A)):
            if(A[j] < A[menor]):
                menor = j
        [A[menor], A[i]] = [A[i], A[menor]]  # Troca
    return A