#include <stdio.h>
#include <stdlib.h>

/*
Umprograma que executa fatorial dos valores entre 1 e 10;
*/
double calcFat(int n);

int main(void)
{

    for (int i = 1; i <= 10; i++)
    {
        printf("%i! = %.2f\n", i, calcFat(i));
    }
    
}

double calcFat(int n) {
    if (n <= 1) {
        return 1;
    }
    else {
        return n * calcFat(n - 1);
    }
}