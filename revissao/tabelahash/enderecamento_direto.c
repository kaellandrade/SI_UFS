#include <stdio.h>
#include <stdlib.h>
#define R 100

void contabiliza(int *tb, int ch);
void imprime(int *tb);
void inicializa(int *tb);

int main()
{
    int *tabela;
    tabela = malloc(R * sizeof(int));

    inicializa(tabela);

    contabiliza(tabela, 1);
    contabiliza(tabela, 1);
    contabiliza(tabela, 1);
    contabiliza(tabela, 1);
    contabiliza(tabela, 1);
    contabiliza(tabela, 1);

    imprime(tabela);

    return 0;
}
void contabiliza(int *tb, int ch)
{
    tb[ch]++;
}

void imprime(int *tb)
{
    for (int i = 0; i < R; i++)
        printf("[%d] = %d\n", i, tb[i]);
    
}
void inicializa(int *tb)
{
    for (int i = 0; i < R; i++)
        tb[i] = 0;
}