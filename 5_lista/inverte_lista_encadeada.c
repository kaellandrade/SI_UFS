/*
NÍVEL: Fácil
Descrição
---------

Escreva uma função para inverter uma lista encadeada usando somente uma "passada" pela lista. 
Formato de entrada
------------------
Uma lista encadeada. Cada nó da lista deve possuir um número.

Formato de saída
----------------
A mesma lista, mas em ordem inversa.
*/

#include <stdio.h>
#include <stdlib.h>
typedef struct reg celula;

struct reg
{
    int conteudo;
    celula *prox;
};

void adiciona(int *p_valor, celula *li);
void inverte(celula *li);
celula *listae;

int main(void)
{
    // Inicializa minha lista
    listae = malloc(sizeof(celula));
    listae->prox = listae;

    int rscan;
    int valor;

    while ((rscan = scanf("%d", &valor)) && (rscan != EOF))
    {
        adiciona(&valor, listae);
    }

    inverte(listae);

    return EXIT_SUCCESS;
}

void adiciona(int *p_valor, celula *li)
{
    celula *nova;
    nova = malloc(sizeof(celula));

    nova->conteudo = (*p_valor);
    nova->prox = li->prox;
    li->prox = nova;
}

void inverte(celula *li)
{
    celula *p = li->prox;
    while (p != li)
    {
        printf(" %d", p->conteudo);
        p = p->prox;
    }
}
