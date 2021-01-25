/*
NÍVEL: Iniciante
Descrição
---------
Você deve intercalar dois arrays de números inteiros.

Formato de entrada
------------------
Na primeira linha você receberá um número inteiro n indicando o tamanho de cada um dos arrays.
As próximas n linhas correspondem aos elementos do primeiro array.
Depois seguirão mais n linhas correspondendo aos elementos do segundo array.

Formato de saída
----------------
Você deve imprimir 2n linhas com os arrays intercalados. Por exemplo, se a entrada for:
3
1
5
9
2
4
8

Você deve imprimir:
1
2
5
4
9
8
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct reg celula;

struct reg
{
    int conteudo;
    celula *prox;
};

celula *addElemento(int *p_valor, celula *fila);
int removeElemento(celula *fila);
celula *intercalaElementos(celula *fila1, celula *fila2, celula *intercalada);
void imprime(celula *fi);

int main(void)
{
    celula *fila, *fila2, *intercalada;
    // Inicializa as filas
    fila = malloc(sizeof(celula));
    fila2 = malloc(sizeof(celula));
    intercalada = malloc(sizeof(celula));

    fila->prox = fila;
    fila2->prox = fila2;
    intercalada->prox = intercalada;

    int tamanho, valor;
    scanf("%d", &tamanho);
    tamanho *= 2;

    for (int i = 0; i < tamanho / 2; i++)
    {
        scanf("%d", &valor);
        fila = addElemento(&valor, fila);
    }

    for (int i = 0; i < tamanho / 2; i++)
    {
        scanf("%d", &valor);
        fila2 = addElemento(&valor, fila2);
    }

    intercalada = intercalaElementos(fila, fila2, intercalada);
    imprime(intercalada);
    return EXIT_SUCCESS;
}

int removeElemento(celula *fila)
{
    int valor;
    celula *p;
    p = fila->prox;
    valor = p->conteudo;
    fila->prox = p->prox;
    free(p);
    return valor;
}

celula *addElemento(int *p_valor, celula *fila)
{
    celula *nova;
    nova = malloc(sizeof(celula));
    nova->prox = fila->prox;
    fila->prox = nova;
    fila->conteudo = (*p_valor);
    return nova;
}

celula *intercalaElementos(celula *fila1, celula *fila2, celula *intercalada)
{
    while (fila1->prox != fila1)
    {

        int x = removeElemento(fila1);
        intercalada = addElemento(&x, intercalada);

        int y = removeElemento(fila2);
        intercalada = addElemento(&y, intercalada);
    }

    return intercalada;
}

void imprime(celula *fi)
{
    celula *p;
    p = fi->prox;
    while (p != fi)
    {
        printf("%d\n", p->conteudo);
        p = p->prox;
    }
}