/**
 * ALGORITMO SIMPLES DE SUBSTRING
 * Referências: https://www.ime.usp.br/~pf/algoritmos/aulas/strma.html
 * */
#include <stdlib.h>
#include <stdio.h>
#define N 6
#define M 1
typedef unsigned char byte;

int inocente(byte a[], int m, byte b[], int n);
int main()
{
    byte texto[N] = "asdkhsadckbakjroiusrsdkjshduehdakjhdehckanckeh akjhdskh kajhukh jhds";
    byte palavra[M] = "hd";
    printf("%d\n", inocente(palavra, M-1, texto, N-1)); // pois o índice começa de 0

    return EXIT_SUCCESS;
}

int inocente(byte a[], int m, byte b[], int n)
{
    int ocorre = 0;
    for (int k = m; k <= n; ++k)
    {
        // a[1..m] casa com b [k-m+1]?
        int i = m, j = k;
        while (i >= 0 && a[i] == b[j])
            --i, --j;
        if (i < 0)
            ++ocorre;
    }
    return ocorre;
}