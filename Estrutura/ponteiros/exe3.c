#include <stdio.h>
#include <stdlib.h>

// Protótipo da função;
void testeVariavel(int x);
void testePonteiro(int *p);

int main()
{

    int teste = 1;
    int *pTeste = &teste;

    testePonteiro(pTeste);

    printf("%d\n", teste);

    return 0;
}

void testeVariavel(int x)
{
    x++;
}

void testePonteiro(int *p)
{
    printf("%d\n", *p);
    ++*p;
}