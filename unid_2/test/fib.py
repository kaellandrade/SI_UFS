def fibonacci(n, F={}):
    '''
        Entrada: Um inteiro N e uma tabela F.
        Saída: Fibonacci n.
    '''
    for i in range(0, n+1):
        if(i <= 1):
            F[i] = i
        else:
            F[i] = F[i-1]+F[i-2]
    return F[n]
print(fibonacci(7))
