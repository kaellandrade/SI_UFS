/**
 * Algoritmo 2: lista encadeada
*/
#include <stdio.h>
#include <stdlib.h>

typedef struct reg celula;
typedef celula * tabelaHash;
struct reg
{
    int chave, ocorr;
    celula *prox;
};

tabelaHash tabela;

void contabiliza(int ch);
void imprimir(tabelaHash tabela);

int main()
{
    tabela = NULL;

    contabiliza(1);
    contabiliza(2);
    contabiliza(2);
    contabiliza(3);
    contabiliza(1000);






    imprimir(tabela);

    return 0;
}

void contabiliza(int ch)
{
    celula *p;
    p = tabela;
    while (p != NULL && p->chave != ch)
        p = p->prox;
    if (p != NULL)
        p->ocorr += 1;
    else
    {
        p = malloc(sizeof(celula));
        p->chave = ch;
        p->ocorr = 1;
        p->prox = tabela;
        tabela = p;
    }
}

void imprimir(tabelaHash tabela)
{
    if (tabela != NULL){
        printf("{ [%d] = %d } -> ", tabela->chave, tabela->ocorr);
        imprimir(tabela->prox);
    }
    if(tabela == NULL)
        printf(" NULL\n\n");
    
}