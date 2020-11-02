#include <stdio.h>
#include <stdlib.h>

/*
    Exibe a sequência de fibonacci de 1 até 10
*/
long fibonacci(int n);

int main(void)
{

    for (int i = 0; i <= 10; i++)
    {
        printf("Fib(%d) = %4.1ld\n", i, fibonacci(i));
    }
    
}

long fibonacci(int n) {
    if (n == 1 || n == 0) {
        return n;
    }
    else {
        return fibonacci(n - 1) + fibonacci(n-2);
    }
}