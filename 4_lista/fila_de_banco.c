/*
NÍVEL: Fácil
Descrição
--------
Fila de banco é sempre uma dor de cabeça. 
No Banco do Brasilo, existem apenas dois caixas para atender as pessoas. 
Porém, toda hora do almoço é um problema, pois existem duas filas de pessoas e um dos funcionários precisa ir comer. Então, as duas filas precisam ser integradas. 
Sempre dá confusão. Para minimizar o problema, o gerente do banco, muito sovina, ao invés de contratar mais um funcionário, propôs a seguinte solução. 
As pessoas da fila do funcionário que foi almoçar devem ser intercaladas com as pessoas da fila do funcionário que ficou trabalhando, a partir da segunda posição. 
E haja confusão!


Formato de entrada
------------------
Consiste dos inteiros n, m e k (0<=n <=10000, 0<=m <=10000, 1<=k<=2) correspondendo, 
respectivamente, a quantidade de pessoas que existem em cada fila e qual foi à fila que o funcionário foi almoçar, 
sendo k=1 para a primeira fila e k=2 para a segunda fila. Seguidos de n inteiros representando as pessoas da primeira 
file e m inteiros representando as pessoas da segunda fila. Os inteiros nunca se repetem.



Formato de saída
----------------
Consiste em uma sequência de inteiros, um em cada linha representando as pessoas da nova fila.
*/
#include <stdio.h>
#include <stdlib.h>
typedef struct reg celula;

struct reg
{
    int conteudo;
    celula *proximo;
};

celula *addFila(int *p_valor, celula *fi);
int tiraFila(celula *fi);
void imprimeFila(celula *fi);
void intercala(int *Pk, celula *c1, celula *c2);

celula *caixa1, *caixa2;

int main(void)
{
    // Inicializa a cabeca da pilha;
    int lengFila1, lengFila2, k, valor;

    caixa1 = malloc(sizeof(celula));
    caixa2 = malloc(sizeof(celula));

    caixa1->proximo = caixa1;
    caixa2->proximo = caixa2;

    // Preenche a primeira fila
    scanf("%d", &lengFila1);
    scanf("%d", &lengFila2);
    scanf("%d", &k);
    // Preenche a primira fila
    while (lengFila1 > 0)
    {
        scanf("%d", &valor);
        caixa1 = addFila(&valor, caixa1);
        lengFila1--;
    }

    // Preenche a segunda fila
    while (lengFila2 > 0)
    {
        scanf("%d", &valor);
        caixa2 = addFila(&valor, caixa2);
        lengFila2--;
    }
    printf("\n\n");
    intercala(&k, caixa1, caixa2);

    return EXIT_SUCCESS;
}

// Devolve o endere?o da cabe?a da fila
celula *addFila(int *p_valor, celula *fi)
{
    celula *nova;
    nova = malloc(sizeof(celula));
    nova->proximo = fi->proximo;
    fi->proximo = nova;
    fi->conteudo = *p_valor;
    return nova;
}

int tiraFila(celula *fi)
{
    int valor;
    celula *p;
    p = fi->proximo;
    valor = p->conteudo;
    fi->proximo = p->proximo;
    free(p);
    return valor;
}

void imprimeFila(celula *fi)
{
    celula *p;
    p = fi->proximo;
    while (p != fi)
    {
        printf("%d\n", p->conteudo);
        p = p->proximo;
    }
}

void intercala(int *Pk, celula *c1, celula *c2)
{
    if ((*Pk) == 2)
    {
        while (c1->proximo != c1 && c2->proximo != c2)
        {
            printf("%d\n", tiraFila(c1));
            printf("%d\n", tiraFila(c2));
        }
    }
    else
    {
        while (c1->proximo != c1 && c2->proximo != c2)
        {
            printf("%d\n", tiraFila(c2));
            printf("%d\n", tiraFila(c1));
        }
    }
    //Imprime o que restar na fila
    imprimeFila(c1);
    imprimeFila(c2);
}