/**
NÍVEL: FÁCIL
Tópicos: estrutura de dados, Árvore, alocação dinâmica, busca

Descrição
--------
Escreva um programa que aceita uma árvore binária, e um inteiro N.
Seu programa deve ser capaz de dizer se existe um nó cujo inteiro é N bem como em que profundidade ele se encontra.

Formato de entrada
------------------
Uma árvore binária, representada da seguinte maneira:
(5(4(11(7()())(2()()))())  (8(13()())(4()(1()()))))

Que é a arvore:
               5
              / \
             /   \
            4     8
           /      /\
          11     13 4
         /  \        \
        7    2        1

E um inteiro N

Formato de saída
----------------
Duas linhas. Em uma delas, você irá dizer ESTA NA ARVORE, 
caso o nó cujo inteiro é N esteja na árvore, e NAO ESTA NA ARVORE, caso contrário. Na outra linha, você irá informar em que profundidade da árvore o nó está. 
Caso não esteja, imprima -1.
*/
#include <stdlib.h>
#include <stdio.h>

typedef struct reg noh;
typedef int boolean;

struct reg
{
    int conteudo;
    int prof;
    noh *esq;
    noh *dir;
};
typedef noh *arvore;

void visita_erd(arvore arv, int valor, int profNod);

arvore lerArvoreRED(arvore raiz);
arvore insere(int valor);

arvore encontrada;

int main()
{
    arvore minha_arvore = NULL;
    int valor;
    minha_arvore = lerArvoreRED(minha_arvore);
    scanf("%d", &valor);

    visita_erd(minha_arvore, valor, 0);

    if (encontrada)
    {
        printf("ESTA NA ARVORE\n");
        printf("%d\n", encontrada->prof);
    }
    else
    {
        printf("NAO ESTA NA ARVORE\n");
        printf("%d", -1);
    }

    return EXIT_SUCCESS;
}

void visita_erd(arvore arv, int valor, int profNod)
{

    if (arv != NULL)
    {
        arv->prof = profNod;

        if (valor == arv->conteudo)
        {
            encontrada = arv;
        }

        visita_erd(arv->esq, valor, profNod + 1);
        visita_erd(arv->dir, valor, profNod + 1);
    }
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
            raiz = insere(valorNUM);
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

arvore insere(int valor)
{
    arvore nova_subAr;
    nova_subAr = malloc(sizeof(arvore));

    nova_subAr->conteudo = valor;

    nova_subAr->dir = NULL;
    nova_subAr->esq = NULL;

    return nova_subAr;
}