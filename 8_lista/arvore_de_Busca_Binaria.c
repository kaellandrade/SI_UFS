/*
NÍVEL: Fácil
Tópicos: estrutura de dados, Árvore, recursão, busca 

Descrição
---------

Escreva um programa que aceita uma árvore binária e retorna VERDADEIRO se for uma árvore de busca binária válida, e FALSO caso contrário.

Formato de entrada
-------------------
Uma árvore de busca binária, representada da seguinte maneira:

(5(4(11(7()())(2()()))()) (8(13()())(4()(1()()))))




Formato de saída
----------------
VERDADEIRO, se a árvore for uma árvore de busca binária.
FALSO, se não for.

*/

/* REPRESENTA��O DE UMA ARVORE
(5(4(11(7()())(2()()))()) (8(13()())(4()(1()()))))
*/
#include <stdlib.h>
#include <stdio.h>
#define true 1
#define false 0

typedef struct noh no;
typedef no *arvore;

struct noh
{
    int conteudo;
    no *esq;
    no *dir;
};

arvore lerArvoreRED(arvore raiz);
arvore criarNo(int valor);
void imprimeRED(arvore raiz);
int eBinaria();
void preencheVETOR(arvore raiz);
int totaldeNOS = 0;
int i = 0;
int *VETOR;
int main()
{
    arvore raiz = NULL;        // inicializa minha �rvore;
    raiz = lerArvoreRED(raiz); // preenche minha �rvore

    VETOR = malloc(sizeof(int) * totaldeNOS);

    preencheVETOR(raiz);

    if (eBinaria() ? printf("VERDADEIRO") : printf("FALSO"));

    // imprimeRED(raiz); //!DEBUG
    printf("\n");
    return 0;
}

arvore lerArvoreRED(arvore raiz)
{
    int valorNUM;
    char carac;

    scanf("%c", &carac);
    if (carac == ' ')
        scanf("%c", &carac);
    if (carac == '(')
    {
        if (scanf("%d", &valorNUM))
        {
            raiz = criarNo(valorNUM);
            totaldeNOS++;
        }
        else
        {
            scanf("%c", &carac);
            return raiz;
        }
        raiz->esq = lerArvoreRED(raiz->esq);
        raiz->dir = lerArvoreRED(raiz->dir);
        scanf("%c", &carac);
    }
    return raiz;
}

arvore criarNo(int valor)
{
    no *novoNO = malloc(sizeof(no));
    novoNO->conteudo = valor;
    novoNO->esq = NULL;
    novoNO->dir = NULL;
    return novoNO;
}
void imprimeRED(arvore raiz) // !DEBUG
{
    printf("(");
    if (raiz != NULL)
    {
        printf("%d", raiz->conteudo);
        imprimeRED(raiz->esq);
        imprimeRED(raiz->dir);
    }
    printf(")");
}

void preencheVETOR(arvore raiz)
{
    if (raiz != NULL)
    {
        preencheVETOR(raiz->esq);
        VETOR[i++] = raiz->conteudo;
        preencheVETOR(raiz->dir);
    }
}

int eBinaria()
{
    for (int i = 1; i < totaldeNOS; i++)
    {
        if (VETOR[i - 1] > VETOR[i])
            return false;
    }
    return true;
}