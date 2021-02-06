/**
 * Algoritmo 3: hashing com encadeamento
*/
#include <stdio.h>
#include <stdlib.h>
#define M 50

typedef struct reg celula;
typedef celula **tabelaHash2;
typedef  celula * listaEnc;
struct reg
{
    int chave;
    celula *prox;
};

tabelaHash2 tabela;

int hash(int ch, int m);
void contabiliza(int ch);
void imprimirTabela(tabelaHash2 tabela);
void imprimirLista(listaEnc le);

int main()
{
    tabela = malloc(M * sizeof(celula *)); // vetor que armazena ponteios para uma lista encadeada;
    int valor;
    while(scanf("%d", &valor) != EOF){
        contabiliza(valor);
    }

    imprimirTabela(tabela);

    return 0;
}

void contabiliza(int ch)
{
    int h = hash(ch, M);
    celula *p = tabela[h];
    while (p != NULL && p->chave != ch)
        p = p->prox;
    if(p == NULL)
    {
        p = malloc(sizeof(celula));
        p->chave = ch;
        p->prox = tabela[h];
        tabela[h] = p;
    }
}

void imprimirLista(listaEnc le)
{
    if (le != NULL){
        printf("{ %d } -> ", le->chave);
        imprimirLista(le->prox);
    }
    if(le == NULL)
        printf(" NULL \n");
    
}
int hash(int ch, int m){
    return (ch % m);
}

void imprimirTabela(tabelaHash2 tabela){
    for (int i = 0; i < M; i++)
       { printf("[%2d] = ", i);imprimirLista(tabela[i]);}
    
}