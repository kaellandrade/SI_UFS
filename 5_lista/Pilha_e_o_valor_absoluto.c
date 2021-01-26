/*
NÍVEL: Fácil
Descrição
----------
Sua tarefa é implementar uma pilha que além de possuir as funções normais de push e pop , deverá conter uma função para retornar em O(1) o valor absoluto da diferença entre o maior e o menor elemento que já foram inseridos na pilha (sem remover o topo).

Formato de entrada
------------------

A entrada será composta de vários comandos nos formatos:
push x
pop
abs

onde o x da entrada "push x" é um inteiro, onde  0 <= x <= 1000 .

obs: não serão dados comandos de pop e abs se a pilha estiver vazia.

Formato de saída
----------------
Para cada comando "pop" você deverá imprimir o topo da pilha.
Para cada comando abs você deverá imprimir o valor absoluto da diferença entre o maior e o menor elemento já inseridos.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct reg
{
    int data;
    struct reg *pProx;
} celula;

celula *pilha;

int estaVazia(celula *p);
void push(int *x);
int abs2(celula *pilha);
int pop(void);

int main(void)
{
    char comando[15], *pcom = &comando[0];
    int valor, *pvalor = &valor;

    pilha = malloc(sizeof(celula));
    pilha->pProx = NULL;
    int res;

    while ((res = scanf("%s", pcom)) && (res != EOF))
    {
        if ((strcmp(pcom, "pop") == 0) && !estaVazia(pilha))
            printf("%d\n", pop());

        if (strcmp(pcom, "push") == 0)
        {
            scanf("%d", pvalor);
            push(pvalor);
        }

        if (strcmp(pcom, "abs") == 0)
            printf("%d\n", abs2(pilha->pProx));
    }

    return EXIT_SUCCESS;
}

int estaVazia(celula *p)
{
    return p->pProx == NULL;
}

void push(int *x)
{
    celula *new;
    new = malloc(sizeof(celula));
    new->data = *x;
    new->pProx = pilha->pProx;
    pilha->pProx = new;
}

int pop(void)
{
    int x;
    celula *lixo;
    lixo = pilha->pProx;
    pilha->pProx = lixo->pProx;
    x = lixo->data;
    free(lixo);

    return x;
}

int abs2(celula *pilha)
{
    int maior = pilha->data;
    int menor = pilha->data;

    for (celula *i = pilha; i != NULL; i = i->pProx)
    {
        if (i->data >= maior)
            maior = i->data;
        if (i->data <= menor)
            menor = i->data;
    }

    return (maior - abs(menor));
}