#include <stdlib.h>
#include <stdio.h>
typedef struct reg noh;
typedef int boolean;

struct reg
{
    int conteudo;
    int chave;
    noh *esq;
    noh *dir;
};
typedef noh *arvore;

// Funções de impressão;
void visita_erd(arvore arv);

// Busca
arvore busca(arvore arv, int valor);

// Inserção
arvore inserir(arvore raiz, int valor);


int main()
{
    arvore minhaArvBusca = inserir(minhaArv,10); // raiz contém esse valor
    minhaArvBusca = inserir(minhaArvBusca,10);


    visita_erd(minhaArv);
    return 0;
}

/**
 * Recebe uma árvore de busca arv e
 * um número valor. 
 * Devolve um nó cuja chave é valor; se tal nó não existe,
 * devolve NULL.
*/
arvore busca(arvore arv, int valor)
{
    if (arv == NULL || arv->chave == valor)
    {
        return arv;
    }
    if (arv->chave > valor)
    {
        return busca(arv->esq, valor);
    }
    else
    {
        return busca(arv->dir, valor);
    }
}

/**
 * Varredura E-R-D ou  inorder traversal, imprimeos elementos em 
 * VISITA
 * 1. a subárvore esquerda da raiz, em ordem e-r-d,
 * 2. a raiz,
 * 3. a subárvore direita da raiz, em ordem e-r-d, 
 * IMPRIME OS VALOES ORDEM ASCENDENTE CASO SEJA UMA ARVORE BINÁRIA DE BUSCA. 
*/
void visita_erd(arvore arv)
{
    if (arv != NULL)
    {
        visita_erd(arv->esq);
        printf("%d, ", arv->chave);
        visita_erd(arv->dir);
    }
}

/**
 * Insere uma valor em uma determinada árvore binária de busca
*/
arvore inserir(arvore raiz, int valor)
{
    if (raiz == NULL)
    { // verifica arvore vazia
        arvore novo = malloc(sizeof(arvore));
        novo->chave = valor;
        novo->dir = NULL;
        novo->esq = NULL;
        return novo;
    }
    else
    {
        if (valor < raiz->chave)
            raiz->esq = inserir(raiz->esq, valor);
        if (valor > raiz->chave)
            raiz->dir = inserir(raiz->dir, valor);
    }
    return raiz;
}