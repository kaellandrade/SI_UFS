def insercaoDireta(A) -> list:
   for i in range(1, len(A)):
        temp = A[i]
        j = i-1
        while((j >= 0) and (A[j] > temp)):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = temp

A = [10,9,8,7,6,5,4,3,2,1,0]
insercaoDireta(A)
print(A)